def main():
    user_input = input("Enter your number: ")
    num = int(user_input)

    if num > 100 or num < 1:
        print("Enter a valid number between 1-100")
        exit()
    while num < 100:
        print(num)
        num = num * 2
    print(num)


if __name__ == "__main__":
    main()
