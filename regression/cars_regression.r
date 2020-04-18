
data(cars)
x = cars$speed
y = cars$dist
n = length(x);
plot(x,y)

	
xbar = sum(x)/n;	  # this is boilerplate taken from simple_regression.r
ybar = sum(y)/n;
xybar = sum(x*y)/n
xsqbar = sum(x*x)/n

b = (ybar*xsqbar-xbar*xybar)/ (xsqbar - xbar*xbar)  # from our calculations
a = (ybar - b)/xbar

abline(b,a)			# add the line that fits the data
				# abline plots line with slope b and y intercept a
cat("a and b are ", a, b, "\n");

# y = ax+b is our modeled relationship between x=speed and y=stopping time
