import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gamma

np.random.seed(1)
data = np.random.gamma(shape=2, scale=3, size=1000)

# Sample moments
m1 = np.mean(data)
m2 = np.var(data)

# Method of moments estimates
beta_hat = m2 / m1
alpha_hat = m1 / beta_hat

# Plot data histogram with fitted density
x = np.linspace(min(data), max(data), 300)
pdf_fit = gamma.pdf(x, a=alpha_hat, scale=beta_hat)

plt.hist(data, bins=30, density=True, alpha=0.6, color='skyblue', edgecolor='black')
plt.plot(x, pdf_fit, 'r-', lw=2, label=f"MoM Fit: α={alpha_hat:.2f}, β={beta_hat:.2f}")
plt.title("Gamma Fit via Method of Moments")
plt.xlabel("x")
plt.ylabel("Density")
plt.legend()
plt.grid(True)
plt.show()