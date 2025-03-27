DAYS_PER_YEAR: int = 365
HOURS_PER_DAY: int = 24
MIN_PER_HOUR: int = 60
SEC_PER_MIN: int = 60
user_input: int = int(input("Please enter how many years you want in seconds: "))

if user_input < 1:
    print("Please enter a number greater than 0!")
    exit()


def main():

    print(
        f"There are {str((DAYS_PER_YEAR * HOURS_PER_DAY * MIN_PER_HOUR * SEC_PER_MIN)*  user_input) } {user_input} in a year!"
    )


if __name__ == "__main__":
    main()
