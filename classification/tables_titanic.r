#  examine various 1-d and 2-d tables with the Titanic data

data(Titanic)    # R just knows about these data
print(dimnames(Titanic)) # the variables and their categorizations
print(Titanic)   # R plots all possible tables for each *fixed* value of last two variables 
print(Titanic["1st","Female",,])   # table of 1st class female by Age and Survival  (conditioning)

print(apply(Titanic, c("Sex","Survived"),sum));  # table on  Sex and Survived
print(apply(Titanic["1st",,,],c("Sex","Survived"),sum))   # table on Sex and Survived for the 1st class



mosaicplot(apply(Titanic, c("Class","Survived"),sum));  # table on  Sex and Survived
mosaicplot(apply(Titanic, c("Class","Sex"),sum));  # table on  Sex and Survived
stopp;

# Interesting Analysis:  Observing 2-way tables of each of "Class","Sex","Age"  with "Survived"
# show that "Female", "Child", and "1st" all had greater survival rates.


mosaicplot(apply(Titanic[,"Female",,], c("Class","Survived"),sum));  # table on  Sex and Survived

# But note that "Female" is more heavily weighted in the higher classes.
# Could it be that "1st"-class passengers just appear to have been favored because they
# contained more Females?
# To consider this, look at the 2-way "Class"x"Survived table separately for both "Female" and "Male".
# Even doing this it appears that "1st" class was was prefered:  





