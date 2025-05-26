import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Seed and parameters
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

fig, ax = plt.subplots(1, 2, figsize=(14, 5), sharey=True)

ax[0].hist(population, bins=30, alpha=0.7, color='lightblue', edgecolor='k')
ax[0].axvline(pop_mean, color='blue', linestyle='dashed', linewidth=2)
ax[0].set_title('Population Distribution')
ax[0].set_xlabel('Value')
ax[0].set_ylabel('Frequency')
ax[0].legend(['Population Mean'])

ax[1].hist(sample, bins=20, alpha=0.7, color='lightgreen', edgecolor='k')
ax[1].axvline(sample_mean, color='green', linestyle='dashed', linewidth=2)
ax[1].axvline(ci[0], color='red', linestyle='dotted', linewidth=2)
ax[1].axvline(ci[1], color='red', linestyle='dotted', linewidth=2)
ax[1].set_title('Sample Distribution')
ax[1].set_xlabel('Value')
ax[1].legend(['Sample Mean', '95% CI'])

plt.suptitle(f"Survey Sampling: Sample Mean = {sample_mean:.2f}, CI = ({ci[0]:.2f}, {ci[1]:.2f})", fontsize=14)
plt.tight_layout()
plt.show()

