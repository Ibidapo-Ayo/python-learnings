import random

choice = input("Roll the dice? (y/n): ").lower()
while True:
    if choice == "y":
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f"({die1}, {die2})")
        choice = input("Roll the dice? (y/n): ").lower()
    elif choice == "n":
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice!")
        choice = input("Roll the dice? (y/n): ").lower()