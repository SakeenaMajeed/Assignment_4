def main():
    list = []

    user_input = input("Enter you word: ")
    print("Your list before: ", list)
    for i in range(3):
        list.append(user_input)

    print("Your list after: ", list)


if __name__ == "__main__":
    main()
