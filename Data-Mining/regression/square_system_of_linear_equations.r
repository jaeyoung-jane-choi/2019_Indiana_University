# Can usually solve a system of n linear equations and n unknowns.
# That is, can usually solve Xa = y
# for a, where X is an nxn matrix and  y,a are n-vectors

n = 10;
X = matrix(rnorm(n*n),ncol=n);
y = rnorm(n)
a = solve(X,y);
e = y - X %*% a;
cat("sq error is ", sum(e*e), "\n");