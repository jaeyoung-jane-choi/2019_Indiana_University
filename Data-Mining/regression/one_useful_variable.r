# Have a single useful variable and 99 garbage variables for prediction response
# when we fit the model we see y = yhat indicating very good predition on training data.
# But model performs badly when we look at new data FROM THE SAME MODEL


# Ridge regression adds complexity penalty to "complexity" of regression coeffs (a)
# 


n = 100
d = 100   # note we have as many predictor variables as observations so likely overfitting
X = matrix(rnorm(n*d),nrow = n, ncol=d);
y = 5*X[,1] + rnorm(n);	   # the relation between the response and predictors only involves 1st predictor variable!
plot(X[,1],y);    # can see obvious relation between first predictor and y

a = solve(t(X) %*% X, t(X) %*% y);
#lambda = .5;      # for ridge regression
#a = solve(t(X) %*% X + lambda*diag(d), t(X) %*% y);   # ridge regression solves different optimization
yhat = X %*% a;

plot(y,yhat);    # perfect prediction.  we should be happy ..... ?


X = matrix(rnorm(n*d),nrow = n, ncol=d);  # try new data from same model
y = 5*X[,1] + rnorm(n);
yhat = X %*% a;				
plot(y,yhat);			# prediction not so good ... but improves with ridge regression

#cat("lambda = ", lambda, " test error = ", sum((y-yhat)^2), "normsq of a = ", sum(a*a), "\n")  # for RR
cat(" test error = ", sum((y-yhat)^2), "normsq of a = ", sum(a*a), "\n")



