
# this example taken from 
# An Introduction to Recursive Partitioning
# Using the RPART Routines
# Terry M. Therneau
# Elizabeth J. Atkinson
# Mayo Foundation

#       the data set:

# pgtime	time to progression, or last follow-up free of progression
# pgstat	status at last follow-up (1=progressed, 0=censored)    our target variable
# age		age at diagnosis
# eet		early endocrine therapy (1=no, 0=yes)
# ploidy	diploid/tetraploid/aneuploid DNA pattern
# g2		% of cells in G2 phase
# grade		tumor grade (1-4)
# gleason	Gleason grade (3-10)



library(rpart);
pairs(stagec);
progstat = factor(stagec$pgstat, levels = 0:1, labels = c("No", "Prog"))
plot(stagec$ploidy,progstat)
plot(progstat,stagec$gleason)
plot(progstat,stagec$g2)
eet = factor(stagec$eet,levels=1:2,labels=c("No","Yes"))
mosaicplot(table(eet,progstat))

fit  = rpart(progstat ~  age + eet + g2 + grade + gleason + ploidy, data = stagec, method ="class",parms = list(split = 'information'))
#fit  = rpart(progstat ~  age + eet + g2 + grade + gleason + ploidy, data = stagec, method ="class",parms = list(split = 'gini'))
print(fit)
#post(fit,file="mytree.ps")
