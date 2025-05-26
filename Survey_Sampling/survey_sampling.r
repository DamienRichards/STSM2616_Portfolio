# R Code: Comparing Stratified vs Simple Sampling + FPC Impact

set.seed(123)

# ----------- Setup ----------- #
# Create synthetic population
N <- 1000
pop1 <- rnorm(500, mean = 40, sd = 5)  # Stratum 1
pop2 <- rnorm(500, mean = 60, sd = 5)  # Stratum 2
population <- c(pop1, pop2)

# Population true mean
pop_mean <- mean(population)

# ----------- 1. Simple Random Sampling ----------- #
n_srs <- 100
srs_sample <- sample(population, n_srs, replace = FALSE)
srs_mean <- mean(srs_sample)
srs_var <- var(srs_sample)
srs_se <- sqrt(srs_var / n_srs * (N - n_srs) / N)  # With FPC

# ----------- 2. Stratified Sampling ----------- #
n1 <- 50; n2 <- 50
sample1 <- sample(pop1, n1)
sample2 <- sample(pop2, n2)

W1 <- length(pop1) / N
W2 <- length(pop2) / N

strat_mean <- W1 * mean(sample1) + W2 * mean(sample2)
strat_se <- sqrt((W1^2 * var(sample1) / n1 + W2^2 * var(sample2) / n2) * (N - n1 - n2) / N)

# ----------- Comparison Plot ----------- #
barplot(height = c(pop_mean, srs_mean, strat_mean),
        names.arg = c("Population", "Simple Sample", "Stratified Sample"),
        col = c("darkgrey", "skyblue", "orchid"),
        main = "Mean Estimates Comparison",
        ylim = c(35, 65))
abline(h = pop_mean, col = "red", lty = 2)

legend("topright", legend = c("True Mean"), col = "red", lty = 2)

# ----------- 3. FPC Comparison Scenarios ----------- #

fpc_comparison <- function(N, n) {
  cat("N =", N, ", n =", n, "\n")
  samp <- sample(population, n)
  var_est <- var(samp)
  se_no_fpc <- sqrt(var_est / n)
  se_with_fpc <- sqrt(var_est / n * (N - n) / N)
  cat("SE without FPC:", round(se_no_fpc, 4), "\n")
  cat("SE with FPC   :", round(se_with_fpc, 4), "\n\n")
}

cat("\n# --- FPC Comparison Scenarios ---\n")
fpc_comparison(N = 200, n = 100)   # Small pop, large sample
fpc_comparison(N = 10000, n = 100) # Large pop, small sample
fpc_comparison(N = 1000, n = 800)  # Small pop, large sample
fpc_comparison(N = 10000, n = 800) # Large pop, large sample
