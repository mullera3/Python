# Python Guessing Game 
# Created by: Amani Muller


from random import randint

number = randint(0,25)


name = input("Welcome to the guessing game! Whats your name? ")

print(f"\n{name} I'm thinking of a number between 1 and 25.\nYou will get 10 chances to guess the number.\nTake a guess!\n")
	

num_guess = 0

while num_guess < 10:
	try:
		x = int(input("Enter a number: "))

	except:
		print("Input not a number! Try again! ")
	else:
		num_guess += 1
		if x < number:
			print('Number to low! ')

		elif x > number:
			print('Number to high! ')

		elif x == number:
			print("Congrats you found the number! ")
			break;

		if num_guess == 10:
			print('\nBetter luck next time!')
			print(f'The number was {number}! ')


	



	

