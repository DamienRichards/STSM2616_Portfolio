# Rao-Blackwell Theorem – Improved R Example (Estimating Mean of Bernoulli)

set.seed(202)

# Simulate Bernoulli sample
n <- 100000
p <- 0.4
X <- rbinom(n, 1, p)

# Rough estimator: mean of 10 randomly chosen elements from the sample
rough_estimator <- function(data, reps = 1000) {
  replicate(reps, mean(sample(data, 10, replace = FALSE)))
}

# Generate rough estimates
rough_vals <- rough_estimator(X)

# Rao-Blackwellized estimator: conditional expectation of rough given sufficient statistic
# For Bernoulli, sufficient statistic is the full sample mean
suff_stat <- mean(X)  # unbiased and sufficient

# The Rao-Blackwellized version of the rough estimator is just the sample mean itself
rb_vals <- rep(suff_stat, length(rough_vals))

# Compare variances and biases
rough_var <- var(rough_vals)
rb_var <- var(rb_vals)
rough_bias <- mean(rough_vals) - p
rb_bias <- mean(rb_vals) - p

cat("\nRough Estimator:   Mean =", mean(rough_vals), ", Var =", rough_var, ", Bias =", rough_bias, "\n")
cat("Rao-Blackwellized: Mean =", mean(rb_vals), ", Var =", rb_var, ", Bias =", rb_bias, "\n")

# Plot comparison
hist(rough_vals, breaks = 30, col = 'lightblue', main = "Rao-Blackwell vs Rough Estimator",
     xlab = "Estimator Values", xlim = c(0.2, 0.6), probability = TRUE)
abline(v = mean(rough_vals), col = 'red', lwd = 2, lty = 2)
abline(v = mean(rb_vals), col = 'darkgreen', lwd = 2, lty = 1)
abline(v = p, col = 'black', lty = 3)
legend("topright", legend = c("Rough Estimator", "Rao-Blackwellized", "True p"),
       col = c("red", "darkgreen", "black"), lwd = 2, lty = c(2, 1, 3))