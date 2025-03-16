library(ggplot2)

plot_binomial_vs_normal = function(n, p) {
    x_vals = seq(0, n, by = 1)
    binomial_cdf = pbinom(x_vals, size = n, prob = p)
    mu = n * p
    sigma = sqrt(n * p * (1 - p))
    normal_cdf = pnorm(x_vals, mean = mu, sd = sigma)
    df = data.frame(x = x_vals, Binomial_CDF = binomial_cdf, Normal_CDF = normal_cdf)
    
    ggplot(df, aes(x)) +
        geom_line(aes(y = Binomial_CDF, color = "Binomial CDF"), linewidth = 1) +
        geom_line(aes(y = Normal_CDF, color = "Normal Approximation"), linetype = "dashed", linewidth = 1) +
        labs(title = paste("Binomial vs Normal Approximation (n =", n, ", p =", p, ")"),
            x = "x", y = "Cumulative Probability") +
        scale_color_manual(values = c("blue", "red")) +
        theme_minimal()
    }

plot_binomial_vs_normal(20, 0.2)
plot_binomial_vs_normal(40, 0.5)