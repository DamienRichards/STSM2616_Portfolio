import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Given values
p = 0.654
n = 25
std_error = np.sqrt(p * (1 - p) / n)

# Define the range for x values (±3 standard deviations around the mean)
x = np.linspace(p - 3 * std_error, p + 3 * std_error, 1000)
y = norm.pdf(x, p, std_error)

# Plotting
plt.figure(figsize=(8, 5))
plt.plot(x, y, label='Sampling Distribution of $\hat{p}$', color='blue')
plt.title('Approximate Sampling Distribution of Sample Proportion')
plt.xlabel('Sample Proportion ($\hat{p}$)')
plt.ylabel('Probability Density')
plt.axvline(p, color='red', linestyle='--', label='Mean ($p = 0.654$)')
plt.axvline(p - std_error, color='green', linestyle='--', label='$\pm 1$ Std Dev')
plt.axvline(p + std_error, color='green', linestyle='--')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
