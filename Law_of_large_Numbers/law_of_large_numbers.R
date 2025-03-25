library(ggplot2)
library(hrbrthemes)

n = 5000
s = runif(n, min=0, max=1)
c_mean = cumsum(s) / 1:n

c_mean = data.frame(c_mean)

ggplot(c_mean, aes(x = 1:n, y = c_mean))+
    geom_line()+
    theme_minimal()




