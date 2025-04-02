library(ggplot2)

# Given data
s1_sq <- 33.25  # Sample 1 variance
s2_sq <- 9.2    # Sample 2 variance
n1 <- 9         # Sample 1 size
n2 <- 11        # Sample 2 size

# Compute F-statistic
F_stat <- s1_sq / s2_sq

# Degrees of freedom
df1 <- n1 - 1
df2 <- n2 - 1

# Critical values
alpha <- 0.05
F_crit_upper <- qf(1 - alpha/2, df1, df2)
F_crit_lower <- qf(alpha/2, df1, df2)

# Create F-distribution data
x_vals <- seq(0, max(F_crit_upper, F_stat) + 1, length.out = 1000)
y_vals <- df(x_vals, df1, df2)
df_data <- data.frame(x = x_vals, y = y_vals)

# Determine closest critical value and set green region
dist_to_lower <- abs(F_stat - F_crit_lower)
dist_to_upper <- abs(F_stat - F_crit_upper)

if (dist_to_lower < dist_to_upper) {
  # F_stat is closer to lower critical value
  green_region <- subset(df_data, x >= min(F_stat, F_crit_lower) & x <= max(F_stat, F_crit_lower))
} else {
  # F_stat is closer to upper critical value
  green_region <- subset(df_data, x >= min(F_stat, F_crit_upper) & x <= max(F_stat, F_crit_upper))
}

# Plot the F-distribution
ggplot(df_data, aes(x, y)) +
  geom_line(color = "blue", size = 1.2) +
  geom_ribbon(data = subset(df_data, x <= F_crit_lower), 
              aes(ymin = 0, ymax = y), fill = "red", alpha = 0.5) +
  geom_ribbon(data = subset(df_data, x >= F_crit_upper), 
              aes(ymin = 0, ymax = y), fill = "red", alpha = 0.5) +
  geom_ribbon(data = green_region, aes(ymin = 0, ymax = y), fill = "green", alpha = 0.5) +
  geom_vline(xintercept = F_stat, color = "black", linetype = "dashed", size = 1) +
  geom_vline(xintercept = F_crit_lower, color = "black", linetype = "dotted", size = 1) +
  geom_vline(xintercept = F_crit_upper, color = "black", linetype = "dotted", size = 1) +
  annotate("text", x = F_crit_lower, y = max(y_vals) * 0.1, 
           label = paste0("Lower Critical Value: ", round(F_crit_lower, 3)), hjust = 1.1, color = "black") +
  annotate("text", x = F_crit_upper, y = max(y_vals) * 0.1, 
           label = paste0("Upper Critical Value: ", round(F_crit_upper, 3)), hjust = -0.1, color = "black") +
  annotate("text", x = F_stat, y = max(y_vals) * 0.2, 
           label = paste0("F-statistic: ", round(F_stat, 3)), hjust = -0.1, color = "black") +
  labs(title = "F-Test: Variance Comparison",
       x = "F-value",
       y = "Density") +
  theme_minimal()


p = 2*pf(F_stat, df1, df2, F, F) 
p
