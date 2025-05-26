import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm

np.random.seed(69)
N = 10000 
shape_param = 5
scale_param = 1.5

# Simulate population yields
population_yields = np.random.gamma(shape=shape_param, scale=scale_param, size=N)
population_yields = population_yields + 2
population_std = np.std(population_yields)

def compute_se_and_ci(sample_size, population_std, N, use_pcf=True):
    sample = np.random.choice(population_yields, size=sample_size, replace=False)
    sample_mean = np.mean(sample)
    sample_std = np.std(sample, ddof=1)

    se_no_pcf = sample_std / np.sqrt(sample_size)
    
    if use_pcf:
        fpc = np.sqrt((N - sample_size) / (N - 1)) 
        se_pcf = se_no_pcf * fpc
    else:
        se_pcf = se_no_pcf
    z = norm.ppf(0.975) 
    ci_no_pcf = (sample_mean - z * se_no_pcf, sample_mean + z * se_no_pcf)
    ci_pcf = (sample_mean - z * se_pcf, sample_mean + z * se_pcf)
    
    # CI width
    ci_width_no_pcf = ci_no_pcf[1] - ci_no_pcf[0]
    ci_width_pcf = ci_pcf[1] - ci_pcf[0]
    
    return se_no_pcf, se_pcf, ci_width_no_pcf, ci_width_pcf
sample_sizes = [10, 50, 100, 500, 1000, 5000, 10000]

se_no_pcf_list = []
se_pcf_list = []
ci_width_no_pcf_list = []
ci_width_pcf_list = []
n_over_N_list = []

for n in sample_sizes:
    se_no_pcf, se_pcf, ci_width_no_pcf, ci_width_pcf = compute_se_and_ci(n, population_std, N, use_pcf=True)
    se_no_pcf_list.append(se_no_pcf)
    se_pcf_list.append(se_pcf)
    ci_width_no_pcf_list.append(ci_width_no_pcf)
    ci_width_pcf_list.append(ci_width_pcf)
    n_over_N_list.append(n / N)

results_df = pd.DataFrame({
    'n/N': n_over_N_list,
    'SE without PCF': se_no_pcf_list,
    'SE with PCF': se_pcf_list,
    'CI width without PCF': ci_width_no_pcf_list,
    'CI width with PCF': ci_width_pcf_list
})

print(results_df)
plt.figure(figsize=(10, 6))
plt.plot(results_df['n/N'], results_df['SE without PCF'], label='SE without PCF', marker='o', linestyle='-', color='red')
plt.plot(results_df['n/N'], results_df['SE with PCF'], label='SE with PCF', marker='o', linestyle='-', color='blue')
plt.xlabel('Sampling Fraction (n/N)')
plt.ylabel('Standard Error')
plt.title('Standard Error with and without Population Correction Factor')
plt.legend()
plt.grid(True)
plt.show()
plt.figure(figsize=(10, 6))
plt.plot(results_df['n/N'], results_df['CI width without PCF'], label='CI width without PCF', marker='o', linestyle='-', color='red')
plt.plot(results_df['n/N'], results_df['CI width with PCF'], label='CI width with PCF', marker='o', linestyle='-', color='blue')
plt.xlabel('Sampling Fraction (n/N)')
plt.ylabel('Confidence Interval Width')
plt.title('Confidence Interval Width with and without PCF')
plt.legend()
plt.grid(True)
plt.show()
