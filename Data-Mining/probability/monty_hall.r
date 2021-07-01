# In the Monty Hall game a money prize is placed behind one of 3 doors. You choose a door you hope
# contains the prize.   Monty then opens one of the remaining doors with no money behind it.  You
# are offered the choice of keeping your door or switching to the remainig unopened door.  Should you switch?

# We estimate the probability of winning according to each strategy.

N = 1000;
stick_win = rep(0,N);		# results of N trials using the "stick with current door" strategy
switch_win = rep(0,N);		# results of N trials using the "switch door" strategy
for (i in 1:N) {
    money  = sample(1:3,1)	# where the money is
    choice = sample(1:3,1)	# door chosen by player
    while (TRUE) {
      show = sample(1:3,1)      # when while loop finished show is empty door shown to player
      if (show != money & show != choice)  break;
    }
    remain = 6 - (show + choice)	# the remaining door.   Should we switch to this one?
    stick_win[i] = (choice == money);
    switch_win[i] = (remain == money);
}

cat("P(stick  wins) = ",sum(stick_win)/N,"\n")
cat("P(switch wins) = ",sum(switch_win)/N,"\n")