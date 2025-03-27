import random

NUM_ROUNDS = 5


def main():
    print("\nWelcome to the High-Low Game!")
    print("--------------------------------\n")

    user_score = 0
    bot_score = 0

    for i in range(5):
        print(f"Round {i + 1}")
        user_random_number = random.randint(1, 100)
        bot_random_number = random.randint(1, 100)

        print(f"\nYour Number is: {user_random_number}")

        guess = input(
            "Do you think your number is higher or lower than the computer's? "
        ).lower()

        while guess != "higher" and guess != "lower":
            guess = input("Please enter either higher or lower: ")

        if (guess == "lower" and user_random_number < bot_random_number) or (
            guess == "higher" and user_random_number > bot_random_number
        ):
            user_score += 1
            print("Congratulations! You guessed it right")
            print(f"Bot guess was: {bot_random_number}")
            print(f"Your Score is: {user_score}")
            print(f"Bot score is: {bot_score}\n")
        else:
            bot_score += 1
            print(
                f"Aww, that's incorrect. The computer's number was: {bot_random_number}"
            )
            print(f"Your Score is: {user_score}")
            print(f"Bot score is: {bot_score}\n")

    print("Your final score is", user_score)
    print("And the bot score is", bot_score)

    if user_score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif user_score > NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")


if __name__ == "__main__":
    main()
