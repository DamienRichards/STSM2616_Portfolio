library(ggplot2)

# Observed and expected absences
observed <- c(23, 16, 14, 19, 28)
expected <- c(20, 20, 20, 20, 20)
days <- c("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")

# Perform the Chi-square goodness-of-fit test
chisq_test <- chisq.test(observed, p = expected / sum(expected))
print(chisq_test)

# Generate Chi-square distribution
x_vals <- seq(0, max(chisq_test$statistic, 9.49) + 5, length.out = 100)
df <- length(days) - 1  # Degrees of freedom
y_vals <- dchisq(x_vals, df)

# Create data frames for plotting
theoretical_data <- data.frame(Chi_Square_Values = x_vals, Density = y_vals)
observed_data <- data.frame(Chi_Square_Statistic = chisq_test$statistic, Density = dchisq(chisq_test$statistic, df))
significance_data <- data.frame(Significance_Level = 9.49, Density = dchisq(9.49, df))

# Define shading areas
shade_x_observed <- seq(chisq_test$statistic, max(x_vals), length.out = 50)
shade_y_observed <- dchisq(shade_x_observed, df)
shade_x_cv <- seq(9.49, max(x_vals), length.out = 50)
shade_y_cv <- dchisq(shade_x_cv, df)

# Plot Chi-square distribution with observed statistic, critical value, and shaded areas
ggplot() +
  geom_line(data = theoretical_data, aes(x = Chi_Square_Values, y = Density), color = "blue", size = 1) +
  geom_vline(data = observed_data, aes(xintercept = Chi_Square_Statistic), color = "red", linetype = "dashed", size = 1) +
  geom_vline(data = significance_data, aes(xintercept = Significance_Level), color = "green", linetype = "dashed", size = 1) +
  geom_ribbon(aes(x = shade_x_observed, ymin = 0, ymax = shade_y_observed), fill = "red", alpha = 0.3) +
  geom_ribbon(aes(x = shade_x_cv, ymin = 0, ymax = shade_y_cv), fill = "green", alpha = 0.3) +
  labs(title = "Chi-square Distribution with Observed Statistic and Critical Value", x = "Chi-square Value", y = "Density") +
  annotate("text", x = chisq_test$statistic + 1, y = max(y_vals) / 2, label = paste("Observed χ² =", round(chisq_test$statistic, 2)), color = "red") +
  annotate("text", x = 9.49 + 1, y = max(y_vals) / 3, label = "Critical Value = 9.49", color = "green") +
  theme_minimal()