# polynomial regression with synthetic data.  First we note that regular linear regression can be accomplished by solving
# the normal equations with the X matrix having two columns: one of them all 1s, the second the predictor variable values.
# Next we note that we can do a quadatric regression (y approx= a + bx + cx^2) by solving the normal equations with
# the X matrix having three columns, oen of all 1s, one of the x values (the predictor variable) and one of the
# squares of the predictor variable.  


n = 100
x = 2*runif(n);
#y = 3 + 4*x  + rnorm(n);
y = 3 + 4*x + 5*x^2 + rnorm(n);
plot(x,y);


#X = cbind(rep(1,n),x)		# cbind is "column bind" -- makes matrix out of columns.
X = cbind(rep(1,n),x,x^2)
a = solve(t(X) %*% X, t(X) %*% y)
yhat = X %*% a
lines(sort(x),sort(yhat));
