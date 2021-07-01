# Can estimate a discrete distribution from a sample by computing the proportion of times each outcome occurs.
# For example, perform the 3 flips of a coin and let X = # Heads.
# There are 4 possible outcomes: 0,1,2,3.
# We sample this experiment and compute the proportion of times each outcome occurs.  


n = 1000    # number of times we simulate
x = rep(0,n);  # will hold the results
for (i in 1:n) {
    x[i] =  sum(runif(3) < .5)
}
print(table(x)/n)  # our estimated probability distribution.
