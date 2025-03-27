import random


def guess_the_number():
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess what it is?")

    number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = input("Enter your guess: ")
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < number:
            print("\nToo low! Try again.\n")
        elif guess > number:
            print("\nToo high! Try again.\n")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break


if __name__ == "__main__":
    guess_the_number()
