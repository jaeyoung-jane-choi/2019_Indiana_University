# fitting of lake erie data with polynomial regression
# can fit a very high-degree polynomial this way

erie = read.csv("/monthly-lake-erie-levels-1921-19.csv",stringsAsFactors=FALSE, sep=",");  # really to 1971!
y = erie[1:600,2]
n = length(y);
x = (1:n)/n       # scale to 0 to 1
plot(x,y)


#X = cbind(rep(1,n),x);
X = cbind(rep(1,n),x,x^2,x^3,x^4,x^5);
a = solve(t(X) %*% X, t(X) %*% y);
yhat = X %*% a;
lines(x,yhat,col=2);
error=y-yhat
cat(sum(error^2))



