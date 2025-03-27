import random

sides: int = 6


def main():

    die1: int = random.randint(1, sides)
    die2: int = random.randint(1, sides)

    total: int = die1 + die2

    print("Dice have", sides, "sides each.")
    print("First die:", die1)
    print("Second die:", die2)
    print("Total of two dice:", total)


if __name__ == "__main__":
    main()
