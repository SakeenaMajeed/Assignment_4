def main(list: list):
    MAX_LENGTH = 3

    while len(list) > MAX_LENGTH:
        removed_element = list.pop(-1)
        print(removed_element)

    print("Your remaining list is:", list)


if __name__ == "__main__":
    example_list = [10, 20, 30, 40, 50]
    main(example_list)
