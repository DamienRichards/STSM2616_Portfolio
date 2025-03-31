n = 100
df_chi = 4
df_t = 10   
df1 = 10     
df2 = 10   

chi_samples = rchisq(n, df = df_chi)
t_samples = rt(n, df = df_t)
f_samples = rf(n, df1 = df1, df2 = df2)

par(mfrow = c(1, 3))  

#chi
hist(chi_samples, 
     breaks = 30,
     main = paste("Chi-square Distribution (df =", df_chi, ")"),
     xlab = "Value",
     col = "lightblue",
     probability = TRUE)
curve(dchisq(x, df = df_chi), 
      add = TRUE, 
      col = "red", 
      lwd = 2)
#t
hist(t_samples,
     breaks = 30,
     main = paste("t-Distribution (df =", df_t, ")"),
     xlab = "Value",
     col = "lightgreen",
     probability = TRUE)
curve(dt(x, df = df_t), 
      add = TRUE, 
      col = "red", 
      lwd = 2)
#f
hist(f_samples,
     breaks = 30,
     main = paste("F-Distribution (df1 =", df1, ", df2 =", df2, ")"),
     xlab = "Value",
     col = "lightpink",
     probability = TRUE)
curve(df(x, df1 = df1, df2 = df2), 
      add = TRUE, 
      col = "red", 
      lwd = 2)
