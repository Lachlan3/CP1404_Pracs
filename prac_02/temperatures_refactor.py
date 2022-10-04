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
            celsius = input("Celsius: ")
            result = celsius_to_fahrenheit(celsius)
            print("Result: {:.2f} F \n".format(result))
        elif choice == "F":
            fahrenheit = input("Fahrenheit: ")
            result = fahrenheit_to_celsius(fahrenheit)
            print("Result: {:.2f} C \n".format(result))
        else:
            print("Invalid option \n")
        print(menu)
        choice = input(">>> ").upper()
    print("Thank you.")


def celsius_to_fahrenheit(celsius):
    result = int(celsius) * 9.0 / 5 + 32
    return result


def fahrenheit_to_celsius(fahrenheit):
    result = 5 / 9 * (int(fahrenheit) - 32)
    return result


main()
