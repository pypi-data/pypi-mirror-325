import pandas as pd
import matplotlib.pyplot as plt
import scanpy as sc
import scipy as sp
import itertools
import numpy as np
import scipy.stats as stats
from sklearn.datasets import make_spd_matrix

import memento.estimator as estimator


def extract_parameters(data, q=0.1, min_mean=0.001):
	"""
		Extract the parameters of real dataset. 
		:data: should be a sparse matrix.
	"""
		
	x_mean, x_var = estimator._hyper_1d_relative(
		data, 
		data.shape[0],
		q=q,
		size_factor=estimator._estimate_size_factor(data, 'hyper_relative', total=True, shrinkage=0.0))
	
	good_idx = np.where(data.mean(axis=0).A1 > min_mean)[0]
	
	Nc = data.sum(axis=1).A1/q
	
	z_mean = x_mean*Nc.mean()
	z_var = (x_var + x_mean**2)*(Nc**2).mean() - x_mean**2*Nc.mean()**2
	
	return (x_mean[good_idx], x_var[good_idx]), (z_mean[good_idx], z_var[good_idx]), Nc, good_idx


def gamma_params_from_moments(m, v):
	
	return m**2/v, v/m


def convert_params_nb(mu, theta):
	"""
	Convert mean/dispersion parameterization of a negative binomial to the ones scipy supports

	See https://en.wikipedia.org/wiki/Negative_binomial_distribution#Alternative_formulations
	"""
	r = theta
	var = mu + 1 / r * mu ** 2
	p = (var - mu) / var
	return r, 1 - p


def simulate_transcriptomes(
	n_cells, 
	means, 
	variances,
	Nc,
	norm_cov=None):
	
	n_genes = means.shape[0]
	
	# Get some parameters for negative binomial
	dispersions = (variances - means)/means**2
	dispersions[dispersions < 0] = 1e-5
	thetas = 1/dispersions
	
	if type(norm_cov) == str:
		return stats.nbinom.rvs(*convert_params_nb(means, thetas), size=(n_cells, n_genes))
		
	# Generate the copula
	n_corr_genes = norm_cov.shape[0]
	gaussian_variables = stats.multivariate_normal.rvs(mean=np.zeros(n_corr_genes), cov=norm_cov, size=n_cells)
	uniform_variables = stats.norm.cdf(gaussian_variables)
	corr_nbinom_variables = stats.nbinom.ppf(uniform_variables, *convert_params_nb(means[:n_corr_genes], thetas[:n_corr_genes]))
	indep_nbinom_variables = stats.nbinom.rvs(*convert_params_nb(means[n_corr_genes:], thetas[n_corr_genes:]), size=(n_cells, n_genes-n_corr_genes))
	nbinom_variables = np.hstack([corr_nbinom_variables, indep_nbinom_variables])
	
	# Generate the cell sizes
	cell_sizes = nbinom_variables.sum(axis=1).reshape(-1,1)#np.random.choice(Nc, size=n_cells).reshape(-1, 1)

	# Construct the transcriptomes
	relative_transcriptome = nbinom_variables/nbinom_variables.sum(axis=1).reshape(-1,1)
	transcriptome = relative_transcriptome*cell_sizes
	
	return np.round(transcriptome).astype(int)


def capture_sampling(transcriptomes, q, q_sq=None, process='hyper', gen=None):
	
	if q_sq is None:
		qs = np.ones(transcriptomes.shape[0])*q
	else:
		m = q
		v = q_sq - q**2
		alpha = m*(m*(1-m)/v - 1)
		beta = (1-m)*(m*(1-m)/v - 1)
		qs = stats.beta.rvs(alpha, beta, size=transcriptomes.shape[0])
	if gen is None:
		gen = np.random.Generator(np.random.PCG64(42343))
	
	if process == 'hyper':
		
		captured_transcriptomes = []
		for i in range(transcriptomes.shape[0]):
			captured_transcriptomes.append(
				gen.multivariate_hypergeometric(transcriptomes[i, :], np.round(qs[i]*transcriptomes[i, :].sum()).astype(int))
			)
		captured_transcriptomes = np.vstack(captured_transcriptomes)
	else: #poisson
		
		captured_transcriptomes = gen.poisson(transcriptomes*qs.reshape(-1, 1))
	
	return qs, captured_transcriptomes


def sequencing_sampling(transcriptomes):
	
	observed_transcriptomes = np.zeros(transcriptomes.shape)
	num_molecules = transcriptomes.sum()
	print(num_molecules)
	
	for i in range(n_cells):
		for j in range(n_genes):
			
			observed_transcriptomes[i, j] = (stats.binom.rvs(n=int(num_reads), p=1/num_molecules, size=transcriptomes[i, j]) > 0).sum()
			
	return observed_transcriptomes