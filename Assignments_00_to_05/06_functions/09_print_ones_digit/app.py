def app(num):
    print("The ones digit is", num % 10)


def main():
    num = int(input("Enter a number: "))
    app(num)


if __name__ == "__main__":
    main()
