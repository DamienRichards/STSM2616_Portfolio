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

pop_binary = np.random.binomial(n=1, p=0.3, size=N)
sample_bin = np.random.choice(pop_binary, size=n, replace=False)
phat = np.mean(sample_bin)
se_prop = np.sqrt(phat * (1 - phat) / n * fpc)
ci_prop = (phat - z * se_prop, phat + z * se_prop)

plt.figure(figsize=(6, 4))
plt.hist(sample_bin, bins=2, color='orchid', edgecolor='k', rwidth=0.8)
plt.xticks([0, 1])
plt.title("Binary Sample Responses (0 = No, 1 = Yes)")
plt.xlabel("Response"); plt.ylabel("Frequency")
plt.grid(True)
plt.show()

print(f"Estimated Proportion: {phat:.3f}")
print(f"95% CI for proportion: [{ci_prop[0]:.3f}, {ci_prop[1]:.3f}]")