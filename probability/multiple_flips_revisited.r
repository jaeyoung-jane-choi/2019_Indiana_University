# Reconsider the problem of estimating P(X = x) where X is the number of H's out of n flips.
# As before, we estimate by simulation, but now we quantify our error as 95% confidence interval


n = 100            # number of times we repeat experiment
x = rep(0,n)	   # will hold results of experiment here
F = 10             # number flips
outcome = 5	   # interested in prob of getting this many H's out of F flips
truep = choose(F,outcome)/2^F
cat("True prob = ",truep, "\n");

for (i in 1:n) {
  x[i] = sum(runif(F)<.5);  # number heads out of F flips
}
error = 1/sqrt(n);
cat("Est. prob = ",  sum(x==outcome)/n, " +-", error , "\n");
  