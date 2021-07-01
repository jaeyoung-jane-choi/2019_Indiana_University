# example to demonstrate overfitting of a classification tree.  

# first create a random feature set with labels that *DO NOT DEPEND ON THE FEATURES*.
# train a decision tree from the data.
# Note there is no way to make a good classifier for this situation

library(rpart)
n = 1000					# number of samples
d = 5					 	# dimension of feature vectors (the many #'s for each obs)
Xtrain = matrix(rnorm(n*d),nrow=n);		# predictor vectors are random #'s
df = data.frame(Xtrain)				# R needs data frames for some operations
ctrain = sample(1:2,n,replace=T)		# the classes for each vector (random)

       	 					# note that the class assigbment doesn't depend on features
						# this means the features can't help in classifying.
#pairs(Xtrain,pch=ctrain,cex=2)
#stopp;
fit = rpart(ctrain ~ Xtrain,method="class",minbucket=1,cp=0,minsplit=2)	# cp = complexity parameter
# fit a decision tree with min terminal size 1 and complexity penalty 0, allowing
# splits of nodes with only 2 examples
# basically this means: keep splitting until there is a single instance at each branch of the tree
print(fit)
plot(fit)	      	       		       # look at the complex tree we built
#stopp;


pred = predict(fit,df,type="vector")		# test the classifier on the training data
trainerrors = sum(pred != ctrain)		#  perfect!!!  ... not surprising
cat("num errors on training = ", trainerrors, "\n");
#stopp;


# now create test data that is *statistically identical* (from same model) to original data

Xtest = matrix(rnorm(n*d),nrow=n);
ctest = sample(1:2,n,replace=T)
df = data.frame(Xtest)
pred = predict(fit,df,type="vector")		# get predicted results from model learned above
testerrors = sum(pred != ctest)			# about 1/2 right! (as you should expect)
cat("num errors on test = ", testerrors, "\n");


# moral:  there was no possible way to get a good predictive model, but the classification tree still
# finds a way to fit the data nearly perfectly.  But this doesn't really accomplish anything
# useful as seen by poor "generalization" (i.e. performance on new data)
# This phenomenom called "overfitting"
