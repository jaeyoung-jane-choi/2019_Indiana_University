# example to show simple linear regression

# first we generate random points that more or less follow a linear relation

n = 100	   	   # number of points
x = rnorm(100);	   # random x values
y = 5*x + 3 + 2.*rnorm(n)  # random y values with approx linear relation  (rnorm centered around 0)
plot(x,y);    		  # observe


xbar = sum(x)/n;	  # we derived our optimal choice for alpha and beta in terms of these
ybar = sum(y)/n;
xybar = sum(x*y)/n
xsqbar = sum(x*x)/n

b = (ybar*xsqbar-xbar*xybar)/ (xsqbar - xbar*xbar)  # from our calculations
a = (ybar - b)/xbar
abline(b,a)			# add the line that fits the data
				# abline plots line with slope b and y intercept a

cat("a and b are ", a, b, "\n");