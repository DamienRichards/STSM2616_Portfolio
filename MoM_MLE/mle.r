# MLE Estimation – R (Poisson Example)

set.seed(42)
data <- rpois(1000000, lambda = 4)

# Log-likelihood function
loglik <- function(lambda) {
  -sum(dpois(data, lambda, log = TRUE))
}

# Optimize
result <- optimize(loglik, interval = c(0.01, 10))
lambda_mle <- result$minimum

# Plot
hist(data, breaks = 0:max(data), freq = FALSE, col = 'lightgreen', border = 'black',
     main = "Histogram with MLE Fit (Poisson)", xlab = "Counts")
lines(0:max(data), dpois(0:max(data), lambda = lambda_mle),
      type = 'h', col = 'red', lwd = 2)
legend("topright", legend = paste("MLE λ =", round(lambda_mle, 2)), col = "red", lwd = 2)
