import random


def choose_word():
    words = [
        "karachi",
        "developer",
        "hangman",
        "challenge",
        "programming",
        "typescript",
        "javascript",
    ]
    return random.choice(words)


def display(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)


def hangman():
    word = choose_word()
    guessed_letters = set()
    guessed_keys = ""
    attempts = 6

    print("Welcome to Hangman! Try to guess the word.")

    while attempts > 0:
        print("\n" + display(word, guessed_letters))
        print(f"\nGuessed letters: {",".join(guessed_keys)}")
        guess = input("Guess a letter: ").lower()

        if guess in guessed_keys:
            print("You already guessed that letter." + "\n")
            continue
        else:
            guessed_keys += guess

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess not in word:
            attempts -= 1
            print(f"Wrong guess! {attempts} attempts left.")

        if set(word).issubset(guessed_letters):
            print(f"\nCongratulations! You guessed the word: {word}")
            return

    print(f"\nGame Over! The word was: {word}")


if __name__ == "__main__":
    hangman()
