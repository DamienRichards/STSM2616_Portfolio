import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

np.random.seed(42)
N = 10000
n = 1000
z = norm.ppf(0.975)

population = np.random.normal(loc=50, scale=10, size=N)

sample = np.random.choice(population, size=n, replace=False)

pop_mean = np.mean(population)
pop_std = np.std(population)
sample_mean = np.mean(sample)
sample_var = np.var(sample, ddof=1)
fpc = (N - n) / N
se = np.sqrt(sample_var / n * fpc)
ci = (sample_mean - z * se, sample_mean + z * se)

stratum1 = np.random.normal(loc=40, scale=5, size=500)
stratum2 = np.random.normal(loc=60, scale=5, size=500)

n1, n2 = 50, 50
sample1 = np.random.choice(stratum1, size=n1, replace=False)
sample2 = np.random.choice(stratum2, size=n2, replace=False)

W1 = len(stratum1) / (len(stratum1) + len(stratum2))
W2 = 1 - W1

strat_mean = W1 * np.mean(sample1) + W2 * np.mean(sample2)

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.hist(stratum1, bins=30, alpha=0.6, color='steelblue', label='Stratum 1')
plt.hist(stratum2, bins=30, alpha=0.6, color='salmon', label='Stratum 2')
plt.axvline(strat_mean, color='black', linestyle='dashed', linewidth=2)
plt.legend()
plt.title("Stratified Population Distributions")
plt.xlabel("Value")

plt.subplot(1, 2, 2)
plt.hist(np.concatenate([sample1, sample2]), bins=30, color='purple', edgecolor='k')
plt.axvline(strat_mean, color='white', linestyle='dashed', linewidth=2)
plt.title("Stratified Sample Distribution")
plt.xlabel("Value")

plt.tight_layout()
plt.show()

print(f"Stratified estimate of mean: {strat_mean:.2f}")


