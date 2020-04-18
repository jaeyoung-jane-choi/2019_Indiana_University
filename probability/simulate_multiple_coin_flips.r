# Suppose X is # of H's in n coin flips.
# We know P(X = x) = choose(n,x)/2^n
# but what if we did't know this?
# Estimate P(X = x) by simulating the experiment



M = 1000000          # number of times we repeat experiment
x = rep(0,M)	   # will hold results of experiment here
n = 10             # number coins
outcome = 5	   # intereted in P(X = outcome)
truep = choose(n,outcome)/2^n
cat("True prob = ",truep, "\n");

for (i in 1:M) {
  x[i] = sum(runif(n)<.5);  # number heads out of n coins
}

cat("Est. prob = ",  sum(x==outcome)/M, "\n");
  