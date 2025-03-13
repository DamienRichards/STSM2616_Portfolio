import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from sympy.parsing.latex import parse_latex

def monte_carlo_integration(func, a, b, N):
    #Perform Monte Carlo integration of func over [a, b] with N samples
    x_samples = np.random.uniform(a, b, N)
    y_samples = func(x_samples)
    integral_estimate = (b - a) * np.mean(y_samples)
    std_dev = np.std(y_samples)
    conf_interval = 1.96 * (b - a) * std_dev / np.sqrt(N)
    return integral_estimate, conf_interval

def plot(true_value, sample_sizes, estimates, conf_intervals):
    #Plot the convergence of Monte Carlo estimates with confidence intervals
    plt.figure(figsize=(8, 5))
    plt.axhline(true_value, color='red', linestyle='--', label=f'True Value: {true_value:.4f}')
    plt.plot(sample_sizes, estimates, marker='o', linestyle='-', color='blue', label='Monte Carlo Estimates')
    plt.fill_between(sample_sizes, estimates - conf_intervals, estimates + conf_intervals,
                    color='blue', alpha=0.2, label='95% Confidence Interval')
    plt.xscale('log')
    plt.xlabel('Sample Size (N)')
    plt.ylabel('Estimated Integral')
    plt.legend()
    plt.title('Monte Carlo Integration Convergence with 95% Confidence Bands')
    plt.show()

def integral(latex, limits, sample_sizes):
    #Perform Monte Carlo integration and compare with true value
    try:
        x = sp.Symbol('x')
        integrand = parse_latex(latex)
        integrand = integrand.rewrite(sp.ln)

        numpy_compatible_modules = {
            "sin": np.sin, "cos": np.cos, "tan": np.tan,
            "asin": np.arcsin, "acos": np.arccos, "atan": np.arctan,
            "sinh": np.sinh, "cosh": np.cosh, "tanh": np.tanh,
            "exp": np.exp, "ln": np.log, "log": np.log,
            "sqrt": np.sqrt, "pi": np.pi, "e": np.e
        }
        f = sp.lambdify(x, integrand, modules=[numpy_compatible_modules])

        a, b = map(float, limits.split(','))

        estimates = []
        conf_intervals = []
        for n in sample_sizes:
            estimate, conf_interval = monte_carlo_integration(f, a, b, n)
            estimates.append(estimate)
            conf_intervals.append(conf_interval)

        true_value = float(sp.integrate(integrand, (x, a, b)).evalf())
        final_estimate = estimates[-1]
        final_error = abs((final_estimate - true_value) / true_value) * 100

        sample_sizes = np.array(sample_sizes)
        estimates = np.array(estimates)
        conf_intervals = np.array(conf_intervals)

        print("\nResults:")
        print(f"True Integral Value: {true_value:.6f}")
        print(f"Monte Carlo Estimate (N={sample_sizes[-1]}): {final_estimate:.6f}")
        print(f"Error Percentage: {final_error:.4f}%")
        plot(true_value, sample_sizes, estimates, conf_intervals)

    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    #Main function to handle user input and execute the integration
    latex_input = input("Enter the definite integral in LaTeX format: ")
    limits_input = input("Enter the limits of integration as 'a,b': ")
    N = int(input("Enter the maximum sample size: "))
        
    if N < 10 or N % 10 != 0:
        raise ValueError("Please enter a sample size that is a power of 10 (e.g., 10, 100, 1000).")

    sample_sizes = [10**i for i in range(1, int(np.log10(N)) + 1)]

    integral(latex_input, limits_input, sample_sizes)

if __name__ == "__main__":
    main()