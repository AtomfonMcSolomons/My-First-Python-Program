import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0

    while guess != random_number:
        guess = int(input(f"Enter a random number between 1 and {x}: "))
        if guess < random_number:
            print("Guess again! The number you guessed is too low")
        elif guess > random_number:
            print("Guess again! The number you guessed is too high")

    print(f"Congratulations! You have guessed the correct number {random_number}.")


