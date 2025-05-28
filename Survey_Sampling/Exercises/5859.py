import numpy as np
import matplotlib.pyplot as plt

# Problem 58: Construct population and simulate sampling distribution
population = np.arange(1, 101)  # Integers from 1 to 100
sample_size = 12
num_samples = 100

# Generate 100 samples and compute means
sample_means = [np.mean(np.random.choice(population, size=sample_size, replace=True)) for _ in range(num_samples)]

# Histogram for Problem 58
plt.figure(figsize=(10, 6))
plt.hist(sample_means, bins=20, color='skyblue', edgecolor='black')
plt.title('Sampling Distribution of Sample Mean (Problem 58)')
plt.xlabel('Sample Mean')
plt.ylabel('Frequency')
plt.axvline(np.mean(population), color='red', linestyle='dashed', linewidth=2, label='Population Mean')
plt.legend()
plt.show()

# Problem 59: Stratified sampling with two and four strata
population_mean = np.mean(population)

# Two strata
stratum_size = 50
stratum_1 = population[:stratum_size]
stratum_2 = population[stratum_size:]
num_strata = 2
samples_per_stratum = 6
stratified_means_2 = []

for _ in range(num_samples):
    sample_1 = np.random.choice(stratum_1, size=samples_per_stratum, replace=True)
    sample_2 = np.random.choice(stratum_2, size=samples_per_stratum, replace=True)
    stratified_mean_2 = (np.mean(sample_1) + np.mean(sample_2)) / num_strata
    stratified_means_2.append(stratified_mean_2)

# Four strata
stratum_size_4 = 25
stratum_1_4 = population[:stratum_size_4]
stratum_2_4 = population[stratum_size_4:2*stratum_size_4]
stratum_3_4 = population[2*stratum_size_4:3*stratum_size_4]
stratum_4_4 = population[3*stratum_size_4:]
num_strata_4 = 4
stratified_means_4 = []

for _ in range(num_samples):
    sample_1_4 = np.random.choice(stratum_1_4, size=samples_per_stratum, replace=True)
    sample_2_4 = np.random.choice(stratum_2_4, size=samples_per_stratum, replace=True)
    sample_3_4 = np.random.choice(stratum_3_4, size=samples_per_stratum, replace=True)
    sample_4_4 = np.random.choice(stratum_4_4, size=samples_per_stratum, replace=True)
    stratified_mean_4 = (np.mean(sample_1_4) + np.mean(sample_2_4) + np.mean(sample_3_4) + np.mean(sample_4_4)) / num_strata_4
    stratified_means_4.append(stratified_mean_4)

# Histograms for Problem 59
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.hist(stratified_means_2, bins=20, color='lightgreen', edgecolor='black')
plt.title('Stratified Mean Distribution (2 Strata)')
plt.xlabel('Stratified Mean')
plt.ylabel('Frequency')
plt.axvline(population_mean, color='red', linestyle='dashed', linewidth=2, label='Population Mean')
plt.legend()

plt.subplot(1, 2, 2)
plt.hist(stratified_means_4, bins=20, color='lightcoral', edgecolor='black')
plt.title('Stratified Mean Distribution (4 Strata)')
plt.xlabel('Stratified Mean')
plt.ylabel('Frequency')
plt.axvline(population_mean, color='red', linestyle='dashed', linewidth=2, label='Population Mean')
plt.legend()

plt.tight_layout()
plt.show()

# Comparison
print(f"Population Mean: {population_mean:.2f}")
print(f"Mean of Sample Means (Problem 58): {np.mean(sample_means):.2f}")
print(f"Mean of Stratified Means (2 Strata): {np.mean(stratified_means_2):.2f}")
print(f"Mean of Stratified Means (4 Strata): {np.mean(stratified_means_4):.2f}")