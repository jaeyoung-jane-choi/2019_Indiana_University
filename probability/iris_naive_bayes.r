#implementation of Naive Bayes classification for Fisher's Iris data.  


data(iris3)   # (different form of same data) 3 dim array,  iris3[50 examples, 4 attributes, 3 classes]

# quantize the data into 4 levels for each feautre

for (f in 1:4) {    	    # for each feature
    bk = quantile(iris3[,f,],c(0,.25,.5,.75,1))  # the 0%, 25% , 50%, 75%, 100% quantiles
    bk[1] = 0;            # kludge for endpoint problem
      iris3[,f,] = cut(iris3[,f,],breaks=bk,labels=1:4)   # substitute the 4 quantized values
}



Q = array(0,dim=c(3,4,4));	# Q[c,f,v] is P(feature f = v | class c)
for (c in 1:3) {
    for (f in 1:4) {
       for (v in 1:4) {
       	   Q[c,f,v] = sum(iris3[,f,c] == v)/50   # estimate probs by usual counting
       }
    }
}


prior = rep(1/3,3);  # prior not very important in this example since data chosen to have 5 examples from each class

for (c in 1:3) {
    for (i in 1:50) {    # for each flower ...
    	p = prior;
    	x = iris3[i,,c];   # the quantized feature values for the ith flower of class c
	for (cc in 1:3) {  # compute posterior likelihood of each class cc
	     for (f in 1:4) {  # for each feature
	           p[cc] = p[cc]*Q[cc,f,x[f]]  # include data likleihood of fth feature under class cc
             }
	}
	p = p/sum(p)  # make them into probs
	cat("true class: ",c,"nb says: ",which.max(p),"\n");
    }
}



