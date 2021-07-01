# choose a probability p as runif (everything in [0,1] ='ly likely)
# simulate two coin flips with P(H) = p
# A = 1st flip H
# B = 2nd flip H
# A,B independent?

N = 100000;
A = rep(0,N);
B = rep(0,N);
p = runif(1);
for (i in 1:N) {    
    A[i] = (runif(1) < p);
    B[i] = (runif(1) < p);
}
cat("estimate of P(A) = ", sum(A)/N, "\n")
cat("estimate of P(A|B) = ", sum(A & B)/sum(B), "\n")
