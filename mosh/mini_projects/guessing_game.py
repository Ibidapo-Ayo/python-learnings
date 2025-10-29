import random
random_number = random.randint(1, 10)

number_of_guesses = 0

while number_of_guesses < 3:
    guess = int(input("Guess a number between 1 and 10: "))
    number_of_guesses += 1
    if guess == random_number:
        print(f"You guessed the number in {number_of_guesses} guesses! You win!")
        break
else:
    print("Sorry ! You didn't guess the number. Try again!") 

