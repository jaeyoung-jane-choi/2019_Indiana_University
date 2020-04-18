# simulate the process of flipping a coin using runif.

# if runif(1) < .5 we say H
# otherwise say T

# We know P(Heads) = .5, but suppose we didn't know this.
# Estimate the probability that experiment results in Heads.


M = 1000  # number of times we replicate experiment
cat("Est. prob = ",sum(runif(M)<.5)/M, "\n")   # count prortion of heads
