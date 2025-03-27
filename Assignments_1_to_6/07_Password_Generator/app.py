import random


def main():
    try:
        user_input = input("How many characters do you want in your password? ")
        user_input = int(user_input)
        if user_input < 12:
            print("Password length should be at least 12 characters.")
        else:
            generate_password()
    except ValueError:
        print("Please enter a valid number.")


def generate_password():
    characters = "qwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*()_+"
    password = "".join(random.choices(characters, k=12))
    print("The Generated Password is", password)


if __name__ == "__main__":
    main()
