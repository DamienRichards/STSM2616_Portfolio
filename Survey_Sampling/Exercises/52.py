import numpy as np
from scipy import stats

# Data for each stratum
stratum_1 = [94, 99, 106, 106, 101, 102, 122, 104, 97, 97]
stratum_2 = [183, 183, 179, 211, 178, 179, 192, 192, 201, 177]
stratum_3 = [343, 302, 286, 317, 289, 284, 357, 288, 314, 276]

# Population sizes
N1, N2, N3 = 1000, 1000, 500
N = N1 + N2 + N3  # Total population size

# Sample means
mean_1 = np.mean(stratum_1)
mean_2 = np.mean(stratum_2)
mean_3 = np.mean(stratum_3)

# Sample variances
var_1 = np.var(stratum_1, ddof=1)
var_2 = np.var(stratum_2, ddof=1)
var_3 = np.var(stratum_3, ddof=1)

# Sample sizes
n1, n2, n3 = 10, 10, 10

# Weighted population mean
population_mean = (N1 * mean_1 + N2 * mean_2 + N3 * mean_3) / N

# Population total
population_total = N1 * mean_1 + N2 * mean_2 + N3 * mean_3

# Standard error of the mean
se_mean = np.sqrt((N1**2 * var_1 / n1 + N2**2 * var_2 / n2 + N3**2 * var_3 / n3) / N**2)

# 90% confidence interval for the mean
z = stats.norm.ppf(0.95)  # 90% CI uses 1.645 for z-score
margin_of_error = z * se_mean
ci_mean_lower = population_mean - margin_of_error
ci_mean_upper = population_mean + margin_of_error

# 90% confidence interval for the total
ci_total_lower = population_total - z * np.sqrt(N1**2 * var_1 / n1 + N2**2 * var_2 / n2 + N3**2 * var_3 / n3)
ci_total_upper = population_total + z * np.sqrt(N1**2 * var_1 / n1 + N2**2 * var_2 / n2 + N3**2 * var_3 / n3)

print(f"Population Mean: {population_mean:.2f}")
print(f"Population Total: {population_total:.2f}")
print(f"90% CI for Mean: ({ci_mean_lower:.2f}, {ci_mean_upper:.2f})")
print(f"90% CI for Total: ({ci_total_lower:.2f}, {ci_total_upper:.2f})")