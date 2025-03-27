def guess_the_number():
    low = 1
    high = 100
    print("Welcome to the number guessing game!")
    print(f"Think of a number between {low} and {high}, and I will guess it.")
    input("Press Enter to continue...")
    guesses = 0  # Initialize guesses outside the loop
    while True:
        guess = (low + high) // 2
        guesses += 1  # Increment guesses here, before the check
        print(f"Is your number {guess}?")

        correct_guess = input(
            "Enter 'h' for higher, 'l' for lower, or 'c' for correct: "
        ).lower()
        if correct_guess == "c":
            print("Congratulations! I guessed your number!")
            print(f"It took me {guesses} guesses to guess your number.")
            break
        elif correct_guess == "h":
            low = guess + 1
        elif correct_guess == "l":
            high = guess - 1
        else:
            print("Invalid input. Please enter 'h', 'l', or 'c'.")

    print("Thanks for playing!")


if __name__ == "__main__":
    guess_the_number()
