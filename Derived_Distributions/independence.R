library(ggplot2)

# Observed frequency table
observed <- matrix(c(76, 143, 91, 147, 109, 64), nrow = 2, byrow = TRUE,
                   dimnames = list(Student = c("Freshman", "Senior"),
                                   Hours = c("0-2 Hrs", "2-4 Hrs", "4-6 Hrs")))

# Expected frequency table
expected <- matrix(c(110, 124, 76, 113, 128, 79), nrow = 2, byrow = TRUE,
                   dimnames = list(Student = c("Freshman", "Senior"),
                                   Hours = c("0-2 Hrs", "2-4 Hrs", "4-6 Hrs")))

# Perform Chi-square test for independence
test_result <- chisq.test(observed, p = expected / sum(expected))
print(test_result)

# Generate Chi-square distribution
df <- (nrow(observed) - 1) * (ncol(observed) - 1)  # Degrees of freedom
x_vals <- seq(0, max(test_result$statistic, 5.99) + 5, length.out = 100)
y_vals <- dchisq(x_vals, df)

# Create data frames for plotting
theoretical_data <- data.frame(Chi_Square_Values = x_vals, Density = y_vals)
observed_data <- data.frame(Chi_Square_Statistic = test_result$statistic, Density = dchisq(test_result$statistic, df))
significance_data <- data.frame(Significance_Level = 5.99, Density = dchisq(5.99, df))

# Define shading areas
shade_x_observed <- seq(test_result$statistic, max(x_vals), length.out = 50)
shade_y_observed <- dchisq(shade_x_observed, df)
shade_x_cv <- seq(5.99, max(x_vals), length.out = 50)
shade_y_cv <- dchisq(shade_x_cv, df)

# Plot Chi-square distribution with observed statistic and critical value
ggplot() +
  geom_line(data = theoretical_data, aes(x = Chi_Square_Values, y = Density), color = "blue", size = 1) +
  geom_vline(data = observed_data, aes(xintercept = Chi_Square_Statistic), color = "red", linetype = "dashed", size = 1) +
  geom_vline(data = significance_data, aes(xintercept = Significance_Level), color = "green", linetype = "dashed", size = 1) +
  geom_ribbon(aes(x = shade_x_observed, ymin = 0, ymax = shade_y_observed), fill = "red", alpha = 0.3) +
  geom_ribbon(aes(x = shade_x_cv, ymin = 0, ymax = shade_y_cv), fill = "green", alpha = 0.3) +
  labs(title = "Chi-square Test for Independence", x = "Chi-square Value", y = "Density") +
  annotate("text", x = test_result$statistic + 1, y = max(y_vals) / 2, label = paste("Observed χ² =", round(test_result$statistic, 2)), color = "red") +
  annotate("text", x = 5.99 + 1, y = max(y_vals) / 3, label = "Critical Value = 5.99", color = "green") +
  theme_minimal()
