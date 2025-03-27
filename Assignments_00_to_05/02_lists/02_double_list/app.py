def main(list: list):
    final_list = []
    for number in list:
        final_list.append(number * 2)
    print(f"The doubled list is {final_list}.")


if __name__ == "__main__":
    main([1, 2, 3, 4])
