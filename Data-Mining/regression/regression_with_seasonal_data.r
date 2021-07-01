# analyze data set of month milk production in POUNDS PER COW
# (need to analyze "per capita")

cow = read.csv("/monthly-milk-production-pounds-p.csv",stringsAsFactors=FALSE, sep=",");
n = 167
y = cow[1:n,2]
plot(y,type="l");


x = 1:n
#X = cbind(rep(1,n),x);
#X = cbind(rep(1,n),x,cos(2*pi*x/12),sin(2*pi*x/12))
X = cbind(rep(1,n),x,x^2,x^3)
a = solve(t(X) %*% X, t(X) %*% y);
yhat = X %*% a;
lines(x,yhat,col=2);