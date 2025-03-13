import numpy as np
import matplotlib.pyplot as plt

def main():
    group_size = 10         
    num_groups = 100         
    num_rounds = 5000                  
    p_values = [0.001, 0.01, 0.05]  

    for p in p_values:
        q = (1 - p) ** group_size
        rand_nums = np.random.rand(num_rounds, num_groups)
        cost_per_group = np.where(rand_nums < q, 10, 110)
        total_cost_per_round = cost_per_group.sum(axis=1)
        mean_cost = np.mean(total_cost_per_round)
        var_cost = np.var(total_cost_per_round)
        print(f"For p = {p}:")
        print(f"  Mean cost: ${mean_cost:.2f}")
        print(f"  Variance of cost: {var_cost:.2f}")
        plot(total_cost_per_round, p)
    
def plot(cost, p):
    plt.hist(cost, bins=30, density=True, color='blue', alpha=0.7)
    plt.title(f"Cost Distribution for p = {p}")
    plt.xlabel("Total Cost ($)")
    plt.ylabel("Density")
    plt.show()

if __name__ == '__main__':
    main()