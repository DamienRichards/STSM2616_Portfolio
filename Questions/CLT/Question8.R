library(ggplot2)

plot_poisson_vs_normal = function(lambda) {
  x_vals = 0:(lambda * 2)  
  poisson_cdf = ppois(x_vals, lambda)
  normal_cdf = pnorm(x_vals, mean = lambda, sd = sqrt(lambda))
  
  df = data.frame(x = x_vals, Poisson_CDF = poisson_cdf, Normal_CDF = normal_cdf)

  ggplot(df, aes(x)) +
    geom_line(aes(y = Poisson_CDF, color = "Poisson CDF"), linewidth = 1) +
    geom_line(aes(y = Normal_CDF, color = "Normal Approximation"), linetype = "dashed", linewidth = 1) +
    labs(title = paste("Poisson vs Normal Approximation (λ =", lambda, ")"),
         x = "x", y = "Cumulative Probability") +
    scale_color_manual(values = c("blue", "red")) +
    theme_minimal()
}


plot_poisson_vs_normal(10)
plot_poisson_vs_normal(20)
plot_poisson_vs_normal(40)
