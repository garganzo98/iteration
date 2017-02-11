def computer_guess(num):
		low = 1
		high = 1000
		guess = 500
		while guess != num:
			guess = (low+high)//2
			print("the computer takes a guess...", guess)
			if guess > num:
				high = guess
			elif guess < num:
				low = guess + 1

	print ("the computer guessed", guess, "and it was correct")

def main():
	num = int(input("enter a number:"))
	if num < 1 or num > 100:
		print("must be in range[1, 1000")
	else:
		computer_guess(num)

if_name__=="_main_":
	main()

