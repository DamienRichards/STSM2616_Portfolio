import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

np.random.seed(42)

def main():
    n = 100  
    p = 0.01
    num_simulations = 5000 

    Y_samples = np.random.binomial(n, p, num_simulations)
    calcultions(Y_samples, n, p)

def calcultions(sample, size, p):
    total_costs = 11000 - 100 * sample
    mean_Y = size * p
    var_Y = size * p * (1 - p)
    mean_cost = 11000 - 100 * mean_Y
    var_cost = (100**2) * var_Y
    std_cost = np.sqrt(var_cost)

    plot(total_costs, mean_cost, std_cost, var_cost)

def plot(tc, mean, std, var):
    plt.hist(tc, bins=50, density=True, alpha=0.7, color='skyblue', label='Simulated Costs')
    x = np.linspace(min(tc), max(tc), 100)
    normal_approx = norm.pdf(x, mean, std)
    plt.plot(x, normal_approx, 'r-', lw=2, label=f'Normal Approx\n(μ={mean:.2f}, σ={std:.2f})')
    plt.title('Distribution of Total Costs\nApproaching Normal via Central Limit Theorem')
    plt.xlabel('Total Cost ($)')
    plt.ylabel('Density')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()

    print(f"Theoretical Mean of Total Costs: {mean:.2f}")
    print(f"Theoretical Variance of Total Costs: {var:.2f}")
    print(f"Theoretical Standard Deviation of Total Costs: {std:.2f}")
    print(f"Sample Mean of Total Costs: {np.mean(tc):.2f}")
    print(f"Sample Standard Deviation of Total Costs: {np.std(tc):.2f}")

if __name__ == '__main__':
    main()
