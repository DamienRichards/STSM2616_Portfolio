import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm

np.random.seed(69)

N = 10000
shape_param = 5
scale_param = 1.5

population_yields = np.random.gamma(shape=shape_param, scale=scale_param, size=N)
population_yields = population_yields + 2

plt.figure(figsize=(10,6))
sns.histplot(population_yields, bins=40, kde=True, color='lightgreen')
plt.title('Simulated Maize Yields for 10,000 Farms')
plt.xlabel('Yield (tons per hectare)')
plt.ylabel('Frequency')
plt.show()

###############################################################################################################

true_mean = np.mean(population_yields)
print(f"True Population Mean: {true_mean:.4f}")

def simulate_sample(population, n, true_mean, use_pcf=True):
    sample = np.random.choice(population, size=n, replace=False)
    sample_mean = np.mean(sample)
    sample_std = np.std(sample, ddof=1)

    se = sample_std / np.sqrt(n)

    if use_pcf:
        fpc = np.sqrt((N - n) / (N - 1))
        se *= fpc
    z = norm.ppf(0.975)
    ci_lower = sample_mean - z * se
    ci_upper = sample_mean + z * se
    ci_width = ci_upper - ci_lower

    covered = (ci_lower <= true_mean) and (ci_upper >= true_mean)
    return sample_mean, se, (ci_lower, ci_upper), ci_width, covered
sample_sizes = [10, 50, 100, 500, 1000, 5000, 10000]
results = []

for n in sample_sizes:
    for _ in range(1):
        mean_no_pcf, se_no_pcf, ci_no_pcf, width_no_pcf, covered_no_pcf = simulate_sample(
            population_yields, n, true_mean, use_pcf=False)
        
        mean_pcf, se_pcf, ci_pcf, width_pcf, covered_pcf = simulate_sample(
            population_yields, n, true_mean, use_pcf=True)
        
        results.append({
            'n': n,
            'Sample Mean': mean_pcf, 
            'SE with PFC': se_pcf,
            'SE without PFC': se_no_pcf,
        })
results_df = pd.DataFrame(results)
results_df.head()
print(results_df)

# Define a dark color for density and a lighter one for CI
density_color = 'darkgreen'
ci_color = 'lightgreen'

for n in sample_sizes:
    # Take one sample
    sample = np.random.choice(population_yields, size=n, replace=False)
    sample_mean = np.mean(sample)
    sample_std = np.std(sample, ddof=1)
    se = sample_std / np.sqrt(n)
    
    # Apply finite population correction (PCF)
    fpc = np.sqrt((N - n) / (N - 1))
    se_with_pcf = se * fpc
    
    # Confidence interval
    z = norm.ppf(0.975)
    ci_lower = sample_mean - z * se_with_pcf
    ci_upper = sample_mean + z * se_with_pcf

    # Create a new figure for each plot
    plt.figure(figsize=(10, 6))
    
    # Plot density
    sns.kdeplot(sample, fill=True, color=density_color, alpha=0.8, linewidth=2)
    
    # Shade the confidence interval (lighter)
    plt.axvspan(ci_lower, ci_upper, color=ci_color, alpha=0.3, label='95% CI')

    # Plot true mean
    plt.axvline(true_mean, color='black', linestyle='-', linewidth=2, label='True Mean')
    
    # Plot sample mean
    plt.axvline(sample_mean, color='red', linestyle='--', linewidth=2, label='Sample Mean')
    
    plt.title(f'Density Plot with 95% CI (n = {n})', fontsize=18, weight='bold')
    plt.xlabel('Yield (tons per hectare)', fontsize=14)
    plt.ylabel('Density', fontsize=14)
    plt.legend(fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
