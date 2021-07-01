# Here is a brief introduction to tables in R, including marginalization and conditioning


data("UCBAdmissions"); # import the data  (R just knows about the UCBAdmissions data)
ucb = UCBAdmissions;   # abbreviate UCBAdmissions
print(dimnames(ucb));  # Have a 3-dimsional table
		       #
		       # Admit:		    2 possible values: Admitted and Rejected
		       # Gender:	    2 possible values: Male and Female
		       # Dept:		    6 possible values: A,B,C,D,E,F
		       #
		       # this gives a total of 2x2x6 = 24 combinations that are tabulated,
		       # eg. Rejected Males from A
		       #     Accepted Females from B

# To get the number of Admited and Female and A

print(ucb["Admitted","Female","A"])

# To get the table of Admitted Females (ie conditioning in Admit = Rejected, Gender = Female)

print(ucb["Rejected","Female",])

# To get the table of  Rejected people (ie conditioning on Admit = Rejected)

print(ucb["Rejected",,])

# To get the table of people applying to department E

ucb[,,"E"]


# Rather than looking at numbers, better to look at plot.
# For a 2-way (2-variable) table can use mosaicplot

mosaicplot(ucb[,,"D"])

# or switching rows and columns (same table)
# (t means "transpose")

mosaicplot(t(ucb[,,"D"]))

# Q: For the people who applied to department "D" do Gender and Admit status appear independent?


# To marginalize table to only Dept.
		
apply(ucb,"Dept",sum);		# note "Dept" is a variable name, not a variable value ("A" ... "F")

# To marginalize table to Dept and Gender

apply(ucb,c("Dept","Gender"),sum)


