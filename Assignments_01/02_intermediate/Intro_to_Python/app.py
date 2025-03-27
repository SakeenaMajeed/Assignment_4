planets = {
    "mercury": 37.6,
    "venus": 88.9,
    "mars": 37.8,
    "jupiter": 236.0,
    "Saturn": 108.1,
    "Uranus": 81.5,
    "Neptune": 114.0,
}


def main():
    user_input = int(input("Enter your weight in Earth: "))
    planet = input("Enter a planet: ").lower()

    while planet not in planets:
        planet = input("Enter a valid planet: ").lower()

    conversion = (planets[planet] / 100) * user_input
    rounded_val = round(conversion, 2)
    print(f"The equivalent weight on {planet} is: {rounded_val}")


if __name__ == "__main__":
    main()
