def main():
    side1: float = float(input("What is the length of first side? "))
    side2: float = float(input("What is the length of second side? "))
    side3: float = float(input("What is the length of third side? "))

    print("The perimeter of the triangle is " + str(side1 + side2 + side3))


if __name__ == "__main__":
    main()
