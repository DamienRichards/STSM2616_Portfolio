import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm

np.random.seed(69)

N = 10000 
shape_param = 4
scale_param = 1.2

population = np.random.gamma(shape=shape_param, scale=scale_param, size=N)

n = 5000 
sample = np.random.choice(population, size=n, replace=False)
sample_mean = np.mean(sample)
sample_std = np.std(sample, ddof=1)

true_mean = np.mean(population)

# Standard errors
se_inf = sample_std / np.sqrt(n)
fpc = np.sqrt((N - n) / (N - 1))
se_finite = se_inf * fpc

# Confidence intervals
z = norm.ppf(0.975)
ci_inf = (sample_mean - z * se_inf, sample_mean + z * se_inf)
ci_finite = (sample_mean - z * se_finite, sample_mean + z * se_finite)

# Create normal densities
x = np.linspace(sample_mean - 4*se_inf, sample_mean + 4*se_inf, 1000)
y_inf = norm.pdf(x, loc=sample_mean, scale=se_inf)
y_finite = norm.pdf(x, loc=sample_mean, scale=se_finite)

# Plot
plt.figure(figsize=(10, 6))
sns.set_style("whitegrid")
plt.plot(x, y_inf, label="Infinite Population SE", color="blue")
plt.fill_between(x, 0, y_inf, color="blue", alpha=0.2)
plt.axvline(ci_inf[0], color="blue", linestyle="--")
plt.axvline(ci_inf[1], color="blue", linestyle="--")
plt.plot(x, y_finite, label="Finite Population SE (with PCF)", color="green")
plt.fill_between(x, 0, y_finite, color="green", alpha=0.2)
plt.axvline(ci_finite[0], color="green", linestyle="--")
plt.axvline(ci_finite[1], color="green", linestyle="--")
plt.axvline(true_mean, color="black", linestyle="-", label="True Mean")
plt.axvline(sample_mean, color="red", linestyle="--", label="Sample Mean")
plt.title("Comparison of Confidence Intervals: Infinite vs Finite Population")
plt.xlabel("Sample Mean Estimate")
plt.ylabel("Density")
plt.legend()
plt.tight_layout()
plt.show()
