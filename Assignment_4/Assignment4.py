import numpy as np
import matplotlib.pyplot as plt
from scipy.special import digamma, polygamma
from scipy.optimize import root_scalar

# Step 2.1: Generate Gamma sample with known parameters
np.random.seed(42)
n = 100
true_alpha = 2
true_beta = 1
sample = np.random.gamma(shape=true_alpha, scale=true_beta, size=n)

# Step 2.2: Method of Moments estimates
sample_mean = np.mean(sample)
sample_var = np.var(sample, ddof=1)
mom_alpha = sample_mean**2 / sample_var
mom_beta = sample_var / sample_mean

# Step 2.3: Maximum Likelihood Estimation
# Solving log(alpha) - psi(alpha) = log(mean) - mean(log(X))
log_mean = np.mean(np.log(sample))
mean_val = sample_mean
target = np.log(mean_val) - log_mean

def mle_alpha_eq(alpha):
    return np.log(alpha) - digamma(alpha) - target

sol = root_scalar(mle_alpha_eq, bracket=[0.01, 10], method='brentq')
mle_alpha = sol.root
mle_beta = mean_val / mle_alpha

# Step 2.4: Plot the sample histogram and fitted densities
x_vals = np.linspace(0, max(sample) + 2, 1000)

# Gamma PDF using MoM
from scipy.stats import gamma
mom_pdf = gamma.pdf(x_vals, a=mom_alpha, scale=mom_beta)
mle_pdf = gamma.pdf(x_vals, a=mle_alpha, scale=mle_beta)


# Settings
n_simulations = 1000
n = 100
true_alpha = 2
true_beta = 1

# Containers for estimates
mom_alphas = []
mom_betas = []
mle_alphas = []
mle_betas = []

# Run simulation
for _ in range(n_simulations):
    sample = np.random.gamma(shape=true_alpha, scale=true_beta, size=n)
    
    # MoM
    sample_mean = np.mean(sample)
    sample_var = np.var(sample, ddof=1)
    mom_alpha = sample_mean**2 / sample_var
    mom_beta = sample_var / sample_mean
    mom_alphas.append(mom_alpha)
    mom_betas.append(mom_beta)
    
    # MLE
    log_mean = np.mean(np.log(sample))
    mean_val = sample_mean
    target = np.log(mean_val) - log_mean

    def mle_alpha_eq(alpha):
        return np.log(alpha) - digamma(alpha) - target

    sol = root_scalar(mle_alpha_eq, bracket=[0.01, 10], method='brentq')
    mle_alpha = sol.root
    mle_beta = mean_val / mle_alpha
    mle_alphas.append(mle_alpha)
    mle_betas.append(mle_beta)

# Convert to arrays
mom_alphas = np.array(mom_alphas)
mom_betas = np.array(mom_betas)
mle_alphas = np.array(mle_alphas)
mle_betas = np.array(mle_betas)

# Compute statistics: bias, variance, MSE
def compute_stats(estimates, true_value):
    bias = np.mean(estimates) - true_value
    variance = np.var(estimates, ddof=1)
    mse = bias**2 + variance
    return bias, variance, mse

mom_alpha_stats = compute_stats(mom_alphas, true_alpha)
mom_beta_stats = compute_stats(mom_betas, true_beta)
mle_alpha_stats = compute_stats(mle_alphas, true_alpha)
mle_beta_stats = compute_stats(mle_betas, true_beta)

print({
    "MoM Alpha": {"Bias": mom_alpha_stats[0], "Variance": mom_alpha_stats[1], "MSE": mom_alpha_stats[2]},
    "MoM Beta": {"Bias": mom_beta_stats[0], "Variance": mom_beta_stats[1], "MSE": mom_beta_stats[2]},
    "MLE Alpha": {"Bias": mle_alpha_stats[0], "Variance": mle_alpha_stats[1], "MSE": mle_alpha_stats[2]},
    "MLE Beta": {"Bias": mle_beta_stats[0], "Variance": mle_beta_stats[1], "MSE": mle_beta_stats[2]},
})
