def main():
    fruits = {
        "apple": 1.5,
        "durian": 50,
        "jackfruit": 80,
        "kiwi": 1,
        "rambutan": 1.5,
        "mango": 5,
    }

    total_cost = 0
    for e in fruits:
        user_input = input(f"How many ({e}) you want? ")
        num = int(user_input)
        total_cost += fruits[e] * num

    print(f"Your total cost is: {total_cost}")


if __name__ == "__main__":
    main()
