# Cramér-Rao Lower Bound – Python (Bernoulli Distribution)

import numpy as np
import matplotlib.pyplot as plt

n = 1000
p_true = 0.3

# Simulate Bernoulli data
data = np.random.binomial(1, p_true, size=n)
p_hat = np.mean(data)

# Sample variance of estimator (MLE for p)
var_est = np.var(data) / n

# CRLB for Bernoulli: Var(p̂) ≥ p(1 - p) / n
crlb = p_true * (1 - p_true) / n

print(f"Sample MLE variance: {var_est:.6f}")
print(f"Cramér-Rao Lower Bound: {crlb:.6f}")

# Visual check via simulation
reps = 1000
phats = [np.mean(np.random.binomial(1, p_true, n)) for _ in range(reps)]

plt.hist(phats, bins=30, density=True, color='orchid', edgecolor='black')
plt.axvline(p_true, color='blue', linestyle='dashed', label='True p')
plt.title("Sampling Distribution of MLE for Bernoulli p")
plt.xlabel("p̂")
plt.ylabel("Density")
plt.legend()
plt.grid(True)
plt.show()
