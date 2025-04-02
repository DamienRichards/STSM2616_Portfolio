birth_weights = c(2.6, 2.7, 3.2, 2.9, 3.0, 3.3, 5.2, 2.3, 4.1, 3.7)
mean(birth_weights)
sd(birth_weights)

t_crit = qt(0.975, df = 9)

t_stat = -0.743
2 * pt(t_stat, df = 9)
