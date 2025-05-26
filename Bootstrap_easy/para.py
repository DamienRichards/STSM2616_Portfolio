# Parametric Bootstrap – Python (Normal Distribution Parameters)

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

np.random.seed(0)
data = np.random.normal(loc=5, scale=2, size=100)

# Estimate parameters from data (MLEs)
mu_hat = np.mean(data)
sigma_hat = np.std(data, ddof=1)

# Parametric bootstrap: simulate from N(mu_hat, sigma_hat)
B = 1000
boot_means = [np.mean(np.random.normal(mu_hat, sigma_hat, size=len(data))) for _ in range(B)]

# Confidence interval for mean
ci = np.percentile(boot_means, [2.5, 97.5])

# Plot
plt.hist(boot_means, bins=30, density=True, color='cornflowerblue', edgecolor='black')
plt.axvline(mu_hat, color='black', linestyle='--', label='MLE Mean')
plt.axvline(ci[0], color='red', linestyle=':', label='2.5%')
plt.axvline(ci[1], color='red', linestyle=':', label='97.5%')

plt.title("Parametric Bootstrap Distribution of Sample Mean")
plt.xlabel("Bootstrap Means")
plt.ylabel("Density")
plt.legend()
plt.grid(True)
plt.show()

print(f"Parametric 95% CI for mean: ({ci[0]:.2f}, {ci[1]:.2f})")