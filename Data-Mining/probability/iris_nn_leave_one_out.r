

data(iris)   # (different form of same data) 3 dim array,  iris3[50 examples, 4 attributes, 3 classes]

d = as.matrix(dist(iris[,1:4]))
n = nrow(iris);

class = as.numeric(iris[,5])
classhat = rep(0,n);
for (i in 1:n) {
    j = which.min(d[i,(1:n) != i])
    classhat[i] = iris[j,5];
}
cat ("error rate = ", sum(class != classhat)/n,"\n");

