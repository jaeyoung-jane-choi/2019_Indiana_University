# demonstration of foward selection of variables.  The model has 100 variables, but only the first
# 5 variables are truly useful.
# But we don't know this. 

# First we loop through all varaibles seeing which variable produces the smallest sse.  This is our first variable
# Then we loop through all *remaining* variables, keeping the first variable found, to see which pair gives the smallest sse
# etc.


n = 100
d = 100;
X = matrix(rnorm(n*d),nrow = n, ncol=d);
truea = c(1:5,rep(0,d-5))    	# note that only the first 5 vars are useful with 5th the most useful
y = X %*% truea + rnorm(n);

used = rep(FALSE,d);		# initially all varaibles available for selection
var = rep(0,d);			# var[j] will be variable chosen in jth round
bestsse = rep(10000000,d);      # bestsse[j] will be best sse from jth round
for (j in 1:d)  {		# choose 1 variable each time through this loop
    for (i in which(used == FALSE)) {
       used[i] = TRUE;
       XX = X[,used];		# take the "used" columns = used variables
       a = solve(t(XX) %*% XX , t(XX) %*% y);
       yhat = XX %*% a;
       error = y-yhat;
       sse = sum(error*error);
       if (sse < bestsse[j]) {	# if we find a better sse, take it
          bestsse[j] = sse;
          var[j] = i;
       }
       used[i] = FALSE;
   }
   used[var[j]] = TRUE;	 # claim the best variable for future iterations of loop
   cat(var[j],'\n')
}
plot(bestsse)

# from the plot we can see that the variables choosen are progressively less useful
# at some point we would cut them off and only take the most useful ones.  