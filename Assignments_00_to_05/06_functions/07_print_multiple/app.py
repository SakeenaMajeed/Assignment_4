def app(string: str, num: int):
    for i in range(num):
        print(string)


def main():
    string = input("Enter the message you want to repeat: ")
    repitition = int(input("How many times you want to repeat it? "))
    app(string, repitition)


if __name__ == "__main__":
    main()
