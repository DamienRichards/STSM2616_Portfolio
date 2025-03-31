
Fund_A = c(6.5, 5.8, 7.2, 4.9, 6.1, 5.5, 7.3, 6.7, 5.2, 7.0, 
            6.4, 5.9, 6.8, 5.7, 7.1, 6.3, 5.6, 6.9, 7.2, 6.0, 
            5.8, 7.3, 6.5, 5.9)
Fund_B = c(4.3, 5.1, 3.8, 5.5, 4.7, 3.9, 5.0, 4.8, 5.3, 4.5, 
            5.2, 4.0, 3.6, 4.9, 4.4, 5.1, 4.3, 4.8, 4.0, 3.7, 
            5.5, 4.1, 4.6, 5.0)

summary(Fund_A)
summary(Fund_B)
par_A = c(mean(Fund_A), sd(Fund_A), length(Fund_A))
par_B = c(mean(Fund_B), sd(Fund_B), length(Fund_B))
par_A
par_B

t_test = t.test(Fund_A, Fund_B, alternative = "greater", var.equal = FALSE)
t_test

Fund_A = as.numeric(Fund_A)
Fund_B = as.numeric(Fund_B)

boxplot(Fund_A, Fund_B, names = c("FundA, FundB"), 
    col = c("lightblue", "lightcoral"), 
    main = "Comparison of Fund Returns", 
    ylab = "Monthly Returns (%)")

plot(density(Fund_A), col = "blue", lwd = 2, main = "Density Plots of Fund Returns", 
    xlab = "Monthly Returns (%)", ylab = "Density", ylim = c(0, 1), xaxt = "n")
    lines(density(Fund_B), col = "red", lwd = 2)
    legend("topright", legend = c("FundA", "FundB"), col = c("blue", "red"), lwd = 2)

library(car)
leveneTest(c(Fund_A, Fund_B), factor(rep(1:2, each = length(Fund_A))))

t_test_result <- t.test(Fund_A, Fund_B, alternative = "greater", var.equal = FALSE)
t_test_result$conf.int

