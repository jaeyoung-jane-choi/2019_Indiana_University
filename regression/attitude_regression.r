# example of multiple linear regression with Chatterjee and Price attitude data

data(attitude)   # R just knows about this dataset
plot(attitude)   # want to predict the overall rating from the measurements:
		 # complaints, priveliges, learning, raises, critical, advance
		 # note "correlations" between some pairs of variables
		 # cor(attitude) shows correlation matrix between variables
X = as.matrix(attitude[,2:7]);  # X has predictor variables
y = as.vector(attitude[,1]);
a = solve(t(X) %*% X, t(X) %*% y)  # the normal equations in R   %*% is matrix multiplication
cat(a, '\n')    	       	      	       	   # is vector of optimal coefficients for prediction y from x
yhat = X %*% a	 # our predictions of y values
error = y - yhat
sse = sum(error*error)  # sum of squared error.  We chose a by minimizing this.  
cat(sse, '\n')

# have following result for a vector:

# complaints  0.62339189
# privileges -0.05847126
# learning    0.34502167
# raises      0.09910353
# critical    0.12930038
# advance    -0.21968958

# model y_i ~ a^t x_i   (a "dot" x_i) 

# this says we get about .62% increase in response for each 1% increase in (good handling of) complaints 
#                        .34% increase in response for each 1% increase in (good handling of) learning
# etc.  



#  now regress using 1st 1 x variable
#      	       	     1st 2 x variables
#      	       	     1st 3 x variables
#	     	 ...

n = nrow(X);

for (d in 1:6) {
  X = as.matrix(attitude[,2:(2+d-1)]);  
  a = solve(t(X) %*% X, t(X) %*% y)  
  yhat = X %*% a	 
  error = y - yhat
  sse = sum(error*error)
  cat("with ", d, " variables  got sse of ", sse, "\n");
}


# note the sse goes down steadily