def mad_libs():
    print("Welcome to Mad Libs! Fill in the blanks:\n")

    place = input("Enter a place: ")
    adjective = input("Enter an adjective: ")
    animal = input("Enter an animal: ")
    verb = input("Enter a verb: ")

    story = (
        f"\nToday I went to the {place} and saw a {adjective} {animal}. It was {verb}!"
    )

    print("\nHere is your Mad Libs story:")
    print(story)


mad_libs()
