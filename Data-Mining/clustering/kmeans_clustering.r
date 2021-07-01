# simple implementation of k-means clustering.  




K = 3	# number of clusters
n = 50  # points in true clusters 
D = 2;	# dimension of vectors (small for visualization's sake)

# create our data for clustering

N = K*n;  # total number of points
cent = array(10*rnorm(K*D),c(K,D));  # cent[k,] is the center for the kth cluster
T = array(rnorm(K*D*D),c(K,D,D));    # T[k,,] is the linear trans (2x2 matrix)
    				     # applied to get the kth cluster
				     # We just use cent and T to generate data
X = matrix(0,nrow=D,ncol=0);
for (k in 1:K) {
    m = cent[k,];
    L = T[k,,];
    for (i in 1:n) X = cbind(X,L %*% rnorm(D)+m);  # each column is observation (feature vect)
}
X = t(X);	# follow usual convention where each row of data matrix is observation
plot(X);


# --------------------------


# K means algorithm ...

proto = X[sample(1:N,K),];	  # proto[k,] will be center (prototype) of kth cluster (intialize randomly)
dist = matrix(0,K,N); 		  # dist[k,i] will be  distance from ith point to kth prototype
cluster = rep(0,N);		  # cluster[i] will be cluster currently asigned to X[i,]

for (iter in 1:10) {  		  # really would iterate until convergence, but this will be long enough
    for (i in 1:N) {		  # compute distance matrix 
    	for (k in 1:K) {  
	    diff = X[i,] - proto[k,];
	    dist[k,i] = sum(diff^2);
        }	    
    	cluster[i] = which.min(dist[,i]);  # assign each point to closest center
    }
    plot(X[,1],X[,2],col=cluster);  # plot using color for the current clusters
    points(proto,pch='x',col=1:K,cex=3);   	 # plot cluster centers as well
    print("estimated (or reestimated) cluster assignment");
    readline();

    for (k in 1:K) {
    	if (sum(cluster == k) == 0) next;
	    if (sum(cluster == k) == 1) next;	# don't reestimate center if only have 0-1 examples
        proto[k,] = colMeans(X[cluster==k,]);   # reestimate kth cluster center
    }
    print("estimated cluster centers");		
    plot(X[,1],X[,2],col=cluster);  		# plot using color for the current clusters
    points(proto,pch='x',col=1:K,cex=3);   	 # plot cluster centers as well
    readline();					# wait for keyboard input (so we can see what happened so far)
}

