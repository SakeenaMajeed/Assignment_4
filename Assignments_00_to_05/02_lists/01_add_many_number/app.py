def main(list: list):
    sum: int = 0
    for number in list:
        sum += number
    print(f"The sum of the numbers in the list is {sum}.")


if __name__ == "__main__":
    main([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
