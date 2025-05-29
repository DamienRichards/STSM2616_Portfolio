import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.special import digamma, gamma
from scipy.optimize import minimize
import scipy

# Check if trigamma is available
try:
    from scipy.special import trigamma
except ImportError:
    print("Warning: trigamma not found in scipy.special. Using numerical approximation.")
    def trigamma(x, h=1e-5):
        return (digamma(x + h) - digamma(x)) / h

# True parameters
true_alpha = 2.0
true_beta = 3.0

# MoM estimator
def mom_estimators(data):
    x_bar = np.mean(data)
    m2 = np.mean(data**2)
    alpha_mom = x_bar**2 / (m2 - x_bar**2)
    beta_mom = (m2 - x_bar**2) / x_bar
    return alpha_mom, beta_mom

# Negative log-likelihood for MLE
def neg_log_likelihood(params, data):
    alpha, beta = params
    n = len(data)
    if alpha <= 0 or beta <= 0:
        return np.inf
    return n * alpha * np.log(beta) + n * np.log(gamma(alpha)) - (alpha - 1) * np.sum(np.log(data)) + np.sum(data) / beta

# MLE estimator
def mle_estimators(data):
    x_bar = np.mean(data)
    initial_guess = [1.0, x_bar]  # Initial guess for alpha and beta
    result = minimize(neg_log_likelihood, initial_guess, args=(data,), method='Nelder-Mead', options={'maxiter': 1000})
    return result.x

# Monte Carlo simulation
def monte_carlo_simulation(sample_sizes, n_replications):
    results = []
    for n in sample_sizes:
        alpha_mom_list, beta_mom_list = [], []
        alpha_mle_list, beta_mle_list = [], []
        for _ in range(n_replications):
            data = np.random.gamma(true_alpha, true_beta, n)
            # MoM
            try:
                alpha_mom, beta_mom = mom_estimators(data)
                if np.isfinite(alpha_mom) and np.isfinite(beta_mom):
                    alpha_mom_list.append(alpha_mom)
                    beta_mom_list.append(beta_mom)
            except:
                continue
            # MLE
            try:
                alpha_mle, beta_mle = mle_estimators(data)
                if np.isfinite(alpha_mle) and np.isfinite(beta_mle):
                    alpha_mle_list.append(alpha_mle)
                    beta_mle_list.append(beta_mle)
            except:
                continue
        # Compute metrics
        results.append({
            'n': n,
            'alpha_mom_bias': np.mean(alpha_mom_list) - true_alpha if alpha_mom_list else np.nan,
            'beta_mom_bias': np.mean(beta_mom_list) - true_beta if beta_mom_list else np.nan,
            'alpha_mom_var': np.var(alpha_mom_list) if alpha_mom_list else np.nan,
            'beta_mom_var': np.var(beta_mom_list) if beta_mom_list else np.nan,
            'alpha_mom_mse': np.mean((np.array(alpha_mom_list) - true_alpha)**2) if alpha_mom_list else np.nan,
            'beta_mom_mse': np.mean((np.array(beta_mom_list) - true_beta)**2) if beta_mom_list else np.nan,
            'alpha_mle_bias': np.mean(alpha_mle_list) - true_alpha if alpha_mle_list else np.nan,
            'beta_mle_bias': np.mean(beta_mle_list) - true_beta if beta_mle_list else np.nan,
            'alpha_mle_var': np.var(alpha_mle_list) if alpha_mle_list else np.nan,
            'beta_mle_var': np.var(beta_mle_list) if beta_mle_list else np.nan,
            'alpha_mle_mse': np.mean((np.array(alpha_mle_list) - true_alpha)**2) if alpha_mle_list else np.nan,
            'beta_mle_mse': np.mean((np.array(beta_mle_list) - true_beta)**2) if beta_mle_list else np.nan
        })
    return pd.DataFrame(results)

# Bootstrap resampling
def bootstrap_ci(data, n_bootstrap=1000, alpha_level=0.05):
    alpha_boot, beta_boot = [], []
    for _ in range(n_bootstrap):
        boot_sample = np.random.choice(data, size=len(data), replace=True)
        try:
            alpha_mle, beta_mle = mle_estimators(boot_sample)
            if np.isfinite(alpha_mle) and np.isfinite(beta_mle):
                alpha_boot.append(alpha_mle)
                beta_boot.append(beta_mle)
        except:
            continue
    # Confidence intervals
    alpha_ci = np.percentile(alpha_boot, [100 * alpha_level / 2, 100 * (1 - alpha_level / 2)]) if alpha_boot else [np.nan, np.nan]
    beta_ci = np.percentile(beta_boot, [100 * alpha_level / 2, 100 * (1 - alpha_level / 2)]) if beta_boot else [np.nan, np.nan]
    # Standard errors
    alpha_se = np.std(alpha_boot) if alpha_boot else np.nan
    beta_se = np.std(beta_boot) if beta_boot else np.nan
    # Bias
    alpha_mle, beta_mle = mle_estimators(data)
    alpha_bias = np.mean(alpha_boot) - alpha_mle if alpha_boot else np.nan
    beta_bias = np.mean(beta_boot) - beta_mle if beta_boot else np.nan
    return alpha_ci, beta_ci, alpha_se, beta_se, alpha_bias, beta_bias

# Run simulation
sample_sizes = [10, 50, 100, 500, 1000]
n_replications = 1000
np.random.seed(42)
results_df = monte_carlo_simulation(sample_sizes, n_replications)

# Plotting
plt.figure(figsize=(12, 8))
plt.subplot(2, 2, 1)
plt.plot(results_df['n'], np.abs(results_df['alpha_mom_bias']), label='MoM α Bias', marker='o')
plt.plot(results_df['n'], np.abs(results_df['alpha_mle_bias']), label='MLE α Bias', marker='s')
plt.xlabel('Sample Size')
plt.ylabel('Absolute Bias')
plt.legend()
plt.grid(True)

plt.subplot(2, 2, 2)
plt.plot(results_df['n'], results_df['alpha_mom_var'], label='MoM α Variance', marker='o')
plt.plot(results_df['n'], results_df['alpha_mle_var'], label='MLE α Variance', marker='s')
plt.xlabel('Sample Size')
plt.ylabel('Variance')
plt.legend()
plt.grid(True)

plt.subplot(2, 2, 3)
plt.plot(results_df['n'], results_df['alpha_mom_mse'], label='MoM α MSE', marker='o')
plt.plot(results_df['n'], results_df['alpha_mle_mse'], label='MLE α MSE', marker='s')
plt.xlabel('Sample Size')
plt.ylabel('MSE')
plt.legend()
plt.grid(True)

plt.subplot(2, 2, 4)
plt.plot(results_df['n'], results_df['beta_mom_mse'], label='MoM β MSE', marker='o')
plt.plot(results_df['n'], results_df['beta_mle_mse'], label='MLE β MSE', marker='s')
plt.xlabel('Sample Size')
plt.ylabel('MSE')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig('gamma_estimators.png')
plt.close()

# Bootstrap for a single sample (n=100)
sample_data = np.random.gamma(true_alpha, true_beta, 100)
alpha_ci, beta_ci, alpha_se, beta_se, alpha_bias, beta_bias = bootstrap_ci(sample_data)

# Asymptotic standard errors
n = len(sample_data)
alpha_mle, beta_mle = mle_estimators(sample_data)
alpha_se_asymptotic = np.sqrt(true_alpha / (n * (true_alpha * trigamma(true_alpha) - 1)))
beta_se_asymptotic = np.sqrt(true_beta**2 * trigamma(true_alpha) / (n * (true_alpha * trigamma(true_alpha) - 1)))

# Print results
print(f"SciPy version: {scipy.__version__}")
print(f"Bootstrap Results (n=100):")
print(f"α MLE: {alpha_mle:.4f}, CI: {alpha_ci}, SE: {alpha_se:.4f}, Bias: {alpha_bias:.4f}")
print(f"β MLE: {beta_mle:.4f}, CI: {beta_ci}, SE: {beta_se:.4f}, Bias: {beta_bias:.4f}")
print(f"Asymptotic SE (α): {alpha_se_asymptotic:.4f}, (β): {beta_se_asymptotic:.4f}")
