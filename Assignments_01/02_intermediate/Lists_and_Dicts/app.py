# Problem : 1


def main():
    fruit_list = ["apple", "banana", "orange", "grape", "pineapple"]
    fruit_list.append("mango")
    print(fruit_list)


main()

# Problem : 2 (Index Game)

random_list = []


def accessing_element(list: list, index: int):
    if index > len(list) - 1:
        print("Invalid index, index out of list range")
    else:
        print(list[index])


def modifying_elements(list: list, index: int, new_val):
    if index > len(list) - 1:
        print("Invalid index, index out of list range")
    else:
        print("List before:", list)
        list[index] = new_val
        print("Modified list", list)


def slicing_list(list: list, start_index: int, end_index: int):
    if IndexError:
        print("Invalid index, index out of list range")
    else:
        print(list[start_index:end_index])


def index_game():
    value = 0
    while len(random_list) != 5:
        arr_value = input(f"Enter your {value} index value: ")
        random_list.append(arr_value)
        value += 1

    print("Your Array is:", random_list)
    user_input = input("Enter an operation (access, modify, slice): ").lower()

    while user_input != "access" and user_input != "modify" and user_input != "slice":
        user_input = input("Enter a valid operation (access, modify, slice): ").lower()

    if user_input == "access":
        ask_index = int(input("What index value you want to access? "))
        accessing_element(random_list, ask_index)
    elif user_input == "modify":
        modiy_index = int(input("What index value you want to access? "))
        modify_new_val = int(input("Enter the value you want to replace: "))
        modifying_elements(random_list, modiy_index, modify_new_val)
    else:
        start_index = int(input("Enter the start index: "))
        end_index = int(input("Enter the end index: "))
        slicing_list(random_list, start_index, end_index)


if __name__ == "__main__":
    index_game()
