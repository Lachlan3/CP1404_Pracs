"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""


def main():
    menu = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
    print(menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius_to_fahrenheit()
        elif choice == "F":
            fahrenheit_to_celsius()
        else:
            print("Invalid option")
        print(menu)
        choice = input(">>> ").upper()
    print("Thank you.")


def celsius_to_fahrenheit():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    print("Result: {:.2f} F".format(fahrenheit))


def fahrenheit_to_celsius():
    fahrenheit = float(input("Fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    # Hint: celsius = 5 / 9 * (fahrenheit - 32)
    # Remove the "pass" statement when you are done. It's a placeholder.
    print("Result: {:.2f} C".format(celsius))


main()
