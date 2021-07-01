# here is an important synthetic example.  We create a collection of predictor variables X that are complete unrelated to
# (independent of) our response variable y.  Thus it is impossible to predict y from X.  Still, when we use more and more
# of these unrelated predictor variables our predictions get better and better.
# that is, our sse is driven to 0.  

n = 100
Z = matrix(rnorm(n*n),nrow=n,ncol=n);
y = rnorm(n)
for (i in 1:n) {
    X = Z[,1:i]
    a = solve(t(X) %*% X, t(X) %*% y);
    yhat = X %*% a
    error = y-yhat
    sse = sum(error*error)
    cat(i, " predictor variables, sse = ", sse, "\n");
}


# this should be no surprise for someone who knows linear algebra.  We have n equations in n unknowns, so we should
# be able to solve for y in terms of the predictors.  That is the matrix equation

#   y = Xa

# where y is the n-length vector of response variables and X is the nxn matrix of predictor variables represents
# n equations in n variables (the a_1, ... a_n)
# in general we can solve such a system perfetly for y, no matter what y is.
# This is another example of overfitting






