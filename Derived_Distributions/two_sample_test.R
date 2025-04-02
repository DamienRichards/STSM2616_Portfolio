# Load necessary package
library(ggplot2)

# Given values
mean_A <- 1.3
mean_B <- 1.6
sd_A <- 0.5
sd_B <- 0.3
n_A <- 22
n_B <- 24

# Calculate t-statistic
t_stat1 <- (mean_A - mean_B) / sqrt((sd_A^2 / n_A) + (sd_B^2 / n_B))
t_stat2 <- 2.44  # Second possible t-value

# Degrees of freedom (conservative estimate)
df <- min(n_A, n_B) - 1

# Compute critical t-values for a 5% significance level (two-tailed)
crit_value <- qt(0.975, df)  # Critical value for 5% significance level

# Generate t-distribution data
x_vals <- seq(-4, 4, length.out = 400)
y_vals <- dt(x_vals, df)
t_data <- data.frame(x = x_vals, y = y_vals)

# Filter data for shading (shade only the tails, NOT between -crit_value and crit_value)
shade_data_left <- subset(t_data, x <= -crit_value)  # Left tail
shade_data_right <- subset(t_data, x >= crit_value)  # Right tail

# Create the plot
ggplot(t_data, aes(x, y)) +
  geom_line(color = "blue") +  
  geom_ribbon(data = shade_data_left, aes(ymax = y), ymin = 0, fill = "red", alpha = 0.5) +
  geom_ribbon(data = shade_data_right, aes(ymax = y), ymin = 0, fill = "red", alpha = 0.5) +
  geom_vline(xintercept = t_stat1, linetype = "dashed", color = "green") +
  geom_vline(xintercept = t_stat2, linetype = "dashed", color = "purple") +
  geom_vline(xintercept = c(-crit_value, crit_value), linetype = "dotted", color = "black") +
  annotate("text", x = t_stat1, y = 0.08, label = paste("t =", round(t_stat1, 2)), 
           color = "green", size = 5, fontface = "bold", hjust = 1.2, vjust = -0.5) +
  annotate("text", x = t_stat2, y = 0.06, label = paste("t =", round(t_stat2, 2)), 
           color = "purple", size = 5, fontface = "bold", hjust = -0.2, vjust = -0.5) +
  annotate("text", x = crit_value, y = 0.03, label = "95%", color = "black", 
           size = 5, fontface = "bold", hjust = -0.3, vjust = -0.5) +
  annotate("text", x = -crit_value, y = 0.03, label = "5%", color = "black", 
           size = 5, fontface = "bold", hjust = 1.3, vjust = -0.5) +
  labs(title = paste("T-distribution with df =", df), x = "t-value", y = "Density") +
  theme_minimal()
