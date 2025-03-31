import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

def main():
    #df1 - chi and t DoF
    #df1 + df2 - f DoF
    df1, df2, sample_size = 5, 10, 10000
    chi_square_samples, t_samples, f_samples = generate_samples(sample_size, df1, df2)
    
    plot_distribution(chi_square_samples, 'chi-square', df1)
    plot_distribution(t_samples, 't', df1)
    plot_distribution(f_samples, 'f', df1, df2)

def generate_samples(sample_size=10000, df1=5, df2=10):
    chi_square_samples = np.random.chisquare(df1, sample_size)
    t_samples = np.random.standard_t(df1, sample_size)
    f_samples = np.random.f(df1, df2, sample_size)
    return chi_square_samples, t_samples, f_samples

def plot_distribution(samples, dist_type, df1, df2=None):
    plt.figure(figsize=(8, 6))
    bins = 50
    density = True
    alpha = 0.6
    
    if dist_type == 'chi-square':
        x = np.linspace(0, max(samples), 1000)
        plt.hist(samples, bins=bins, density=density, alpha=alpha, color='b', label='Simulated')
        plt.plot(x, stats.chi2.pdf(x, df1), 'r-', label='Theoretical')
        plt.title(f'Chi-Square Distribution (df={df1})')
    elif dist_type == 't':
        x = np.linspace(-5, 5, 1000)
        plt.hist(samples, bins=bins, density=density, alpha=alpha, color='g', label='Simulated')
        plt.plot(x, stats.t.pdf(x, df1), 'r-', label='Theoretical')
        plt.title(f't-Distribution (df={df1})')
    elif dist_type == 'f':
        x = np.linspace(0, max(samples), 1000)
        plt.hist(samples, bins=bins, density=density, alpha=alpha, color='purple', label='Simulated')
        plt.plot(x, stats.f.pdf(x, df1, df2), 'r-', label='Theoretical')
        plt.title(f'F-Distribution (df1={df1}, df2={df2})')
    
    plt.legend()
    plt.xlabel('Value')
    plt.ylabel('Density')
    plt.grid()
    plt.savefig(f'{dist_type}_distribution.png')
    plt.show()

if __name__ == "__main__":
    main()