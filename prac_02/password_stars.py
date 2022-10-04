def main():
    password = get_password()
    print_asterisks(password)


def print_asterisks(password):
    print("*" * len(password))


def get_password():
    password = input("Please Enter Password: ")
    while len(password) < 8:
        print("Minimum 8 Characters \n")
        password = input("Please Enter Password: ")
    return password


main()
