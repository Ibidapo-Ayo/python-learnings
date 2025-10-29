import random
random_number = random.randint(1, 100)

while True:
    try:
         number = int(input("Guess a number between 1 and 100: "))
         if number == random_number:
                print("Congratulations! You guessed the number!")
                break
         if number < random_number:
                print("Too low!")
                continue
         if number > random_number:
                print("Too high!")
                continue
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
        continue
