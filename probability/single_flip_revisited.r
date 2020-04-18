# Looking again at estimating P(Heads), this time quantifying our estimation error
# This is usually known as the 95% confidence interval


n = 1000
error = 1/sqrt(n)
cat("Est. prob = ",sum(runif(n)<.5)/n, " +- ", error,  "\n")   # count prortion of heads
