"""
File: coin_flip_runs.py
Name: Feng An Chi
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random


def main():
	"""
	TODO: random get the coin flip (H or T)
	      the string if has continuous result equle to the user's input
	      then stop and print the result string
	"""
	print("Let's flip a coin!")
	num_run = int(input('Number of runs: '))
	c = ""
	dice_run = 0
	is_in_a_row = False
	dice1 = random.randrange(1, 3)
	if dice1 % 2 == 0:
		c += "T"
	else:
		c += "H"
	while True:
		dice2 = random.randrange(1, 3)
		if dice2 % 2 == 0:
			c += "T"
		else:
			c += "H"
		if dice1 % 2 == dice2 % 2:
			if not is_in_a_row:
				dice_run += 1
				is_in_a_row = True
		else:
			is_in_a_row = False
		dice1 = dice2
		if dice_run == num_run:
			break
	print(c)


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
	main()
