def main():
    list = []
    val = input("Enter your value: ")
    while val:
        list.append(val)
        val = input("Enter your value: ")

    print("Here is Your List: ", list)


if __name__ == "__main__":
    main()
