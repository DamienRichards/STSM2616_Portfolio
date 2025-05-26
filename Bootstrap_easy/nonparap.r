# Non-Parametric Bootstrap – R (Median CI from Skewed Data)

set.seed(123)
data <- rexp(50000, rate = 1/10)  # Skewed data (Exponential distribution)

# Original median
theta_hat <- median(data)

# Bootstrap
B <- 1000
boot_medians <- replicate(B, median(sample(data, replace = TRUE)))

# Percentile CI
ci <- quantile(boot_medians, probs = c(0.025, 0.975))

# Plot
hist(boot_medians, breaks = 30, col = "lightblue", border = "white",
     main = "Non-Parametric Bootstrap: Median CI",
     xlab = "Bootstrap Medians")
abline(v = theta_hat, col = "blue", lwd = 2, lty = 2)
abline(v = ci[1], col = "red", lty = 3)
abline(v = ci[2], col = "red", lty = 3)
legend("topright", legend = c("Sample Median", "2.5% CI", "97.5% CI"),
       col = c("blue", "red", "red"), lty = c(2, 3, 3), lwd = 2)

cat("Non-parametric 95% CI for median:", round(ci[1], 2), "to", round(ci[2], 2), "\n")
