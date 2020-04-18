# data on Chilean election for Pinochet in 1988.

x = read.csv2("./chilean_voting.csv",stringsAsFactors=FALSE,sep=",");
vote = 9;        # the vote (Y,N,A,U) is 9th column							
education = 6;   # education is the 6th column
gender = 4;
region = 2;
yes = (x[,vote] == "Y" & !(is.na(x[,vote])))   # boolean vector giving "Yes" voters who are not missing
no = (x[,vote] == "N" & !(is.na(x[,vote])))

x = x[no | yes,]



#t = table(x[,c(gender,vote)])

#t = table(x[,c(region,vote)])
#t = table(x[,c(education,vote)])
t = table(x[,c(education,gender,vote)])
#t = table(x[,c(education,gender,region,vote)])
print(t)
#mosaicplot(t)
#cond_prob = prop.table(t,1);

(t['P','F','N'])

