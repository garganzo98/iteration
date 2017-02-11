import random

guessestaken = 0 

print("Hello,whats your name") 
myName = raw_input()

number=random.randint(1,1000)
print("well," + myName+ "i am thinking of a number between 1 and 1000.")

while guessestaken < 6:
	print("take a guess")
	guess=input()
	guess=int(guess)

	guessestaken = guessestaken + 1

	if guess < number:
		print("sorry, your guess is too low bruh")

	if guess > number:
		print("sorry, your guess is too high my guy")

	if guess == number:
		break 

if guess == number:
	guessestaken=str(guesstaken)
	print("good job," + "you guessed my number in" + guessestaken + "guesses")

if guess !=number:
	number = str(number)
	print("nah fam. the number i was thinking of was" + number)