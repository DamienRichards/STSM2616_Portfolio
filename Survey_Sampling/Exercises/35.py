import numpy as np
import scipy.stats as stats

# Sample data
sample = np.array([
    104, 109, 111, 109, 87,
    86,  80, 119,  88, 122,
    91, 103,  99, 108, 96,
    104, 98,  98,  83, 107,
    79,  87,  94,  92, 97
])

N = 2000  # Population size
n = len(sample)  # Sample size

# Part (a): Unbiased estimate of the population mean
x_bar = np.mean(sample)

# Part (b): Unbiased estimate of population variance and Var(X̄)
s2 = np.var(sample, ddof=1)         # Sample variance (unbiased)
var_xbar = s2 * (1 - n/N) / n       # Finite population correction applied

# Part (c): 95% Confidence Intervals
t_crit = stats.t.ppf(0.975, df=n-1)  # two-sided t critical value

# CI for population mean
margin_mean = t_crit * np.sqrt(var_xbar)
ci_mean = (x_bar - margin_mean, x_bar + margin_mean)

# CI for population total = mean * N
total_estimate = x_bar * N
margin_total = margin_mean * N
ci_total = (total_estimate - margin_total, total_estimate + margin_total)

# Output results
print(f"(a) Estimated population mean: {x_bar:.3f}")
print(f"(b) Estimated population variance: {s2:.3f}")
print(f"    Estimated Var(X̄): {var_xbar:.3f}")
print(f"(c) 95% CI for population mean: {ci_mean}")
print(f"    95% CI for population total: {ci_total}")
