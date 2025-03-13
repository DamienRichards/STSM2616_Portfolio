import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)
POPULATION_SIZE = 1_000_000
#distribution choice
def get_distribution_choice():
    print("Choose a population distribution:")
    print("1: Uniform")
    print("2: Exponential")
    print("3: Gamma")
    print("4: Beta")
    while True:
        try:
            choice = int(input("Enter the number (1-4): "))
            if choice in [1, 2, 3, 4]:
                return choice
        except ValueError:
            print("Invalid input. Please enter an integer between 1 and 4.")
#userinputs
def get_sample_parameters():
    while True:
        try:
            sample_size = int(input("Enter the sample size: "))
            if sample_size > 0:
                break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
    
    while True:
        try:
            num_samples = int(input("Enter the number of samples: "))
            if num_samples > 0:
                break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
    
    return sample_size, num_samples

def get_uniform_params():
    while True:
        try:
            low = float(input("Enter the lower bound for Uniform distribution: "))
            high = float(input("Enter the upper bound for Uniform distribution: "))
            if low < high:
                break
        except ValueError:
            print("Invalid input. Please enter numerical values.")
    return low, high

def get_exponential_params():
    while True:
        try:
            scale = float(input("Enter the scale parameter for Exponential distribution: "))
            if scale > 0:
                break
        except ValueError:
            print("Invalid input. Please enter a positive numerical value.")
    return scale

def get_gamma_params():
    while True:
        try:
            shape = float(input("Enter the shape parameter for Gamma distribution: "))
            scale = float(input("Enter the scale parameter for Gamma distribution: "))
            if shape > 0 and scale > 0:
                break
        except ValueError:
            print("Invalid input. Please enter positive numerical values.")
    return shape, scale

def get_beta_params():
    while True:
        try:
            a = float(input("Enter the 'a' parameter for Beta distribution: "))
            b = float(input("Enter the 'b' parameter for Beta distribution: "))
            if a > 0 and b > 0:
                break
        except ValueError:
            print("Invalid input. Please enter positive numerical values.")
    return a, b

dist_choice = get_distribution_choice()
sample_size, num_samples = get_sample_parameters()

dist_names = {1: "Uniform", 2: "Exponential", 3: "Gamma", 4: "Beta"}
chosen_dist = dist_names[dist_choice]

# Get distribution parameters based on user choice and generate population
if dist_choice == 1:
    low, high = get_uniform_params()
    population = np.random.uniform(low=low, high=high, size=POPULATION_SIZE)
elif dist_choice == 2:
    scale = get_exponential_params()
    population = np.random.exponential(scale=scale, size=POPULATION_SIZE)
elif dist_choice == 3:
    shape, scale = get_gamma_params()
    population = np.random.gamma(shape=shape, scale=scale, size=POPULATION_SIZE)
elif dist_choice == 4:
    a, b = get_beta_params()
    population = np.random.beta(a=a, b=b, size=POPULATION_SIZE)

# Step 1
sample_means = []
for _ in range(num_samples):
    sample = np.random.choice(population, size=sample_size, replace=True)
    sample_means.append(np.mean(sample))
# Step 2
plt.figure(figsize=(14, 6))
# Plot 1
plt.subplot(1, 2, 1)
sns.histplot(population, bins=50, kde=True, color='skyblue', stat='density')
plt.title(f'Population Distribution ({chosen_dist})')
plt.xlabel('Value')
plt.ylabel('Density')
# Plot 2
plt.subplot(1, 2, 2)
sns.histplot(sample_means, bins=50, kde=True, color='salmon', stat='density')
plt.title(f'Distribution of Sample Means\n(n={sample_size}, samples={num_samples})')
plt.xlabel('Sample Mean')
plt.ylabel('Density')
plt.tight_layout()
plt.show()
# Step 3
mean_of_sample_means = np.mean(sample_means)
print(f"Mean of sample means: {mean_of_sample_means:.2f}")