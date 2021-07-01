# A rare disease is present in .1% of population.  We have a good test
# for the disease that tests postive (+) when the person has the disease
# with prob. .99.  Likewise when the person does not have the disease the
# test gives a negative result (-) also with prob. .99.  Suppose a
# random person tests +.  What is the prob. the person has disease?
# That is, what is P(Disease | +)
# We showed in class that this is about 1/11.  Here is a simulation of
# the experiment and an approx of P(Disease | +) by counting.
# Note that the actual instances of the + result are mostly due
# to false positives (+ result when disease not present)

N = 100000
D = rep(FALSE,N);
T = rep(FALSE,N);
for (i in 1:N) {
    D[i] = (runif(1) < .001)  # D is boolean variable for disease
    if (D[i]) {
       T[i] = (runif(1) < .99);
    }
    else {
      T[i] = (runif(1) < .01)
    }
}
cat("estimate of P(D | +) = ", sum(D&T) / sum(T) , "\n");