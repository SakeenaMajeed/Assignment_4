def sum_of_two():
    print("This program will add two numbers.")
    num1: str = input("Enter first number: ")
    num1: int = int(num1)
    num2: str = input("Enter second number: ")
    num2: int = int(num2)
    total: int = num1 + num2
    print("The total is " + str(total) + ".")


if __name__ == "__main__":
    sum_of_two()
