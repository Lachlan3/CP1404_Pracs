def main():

    menu = """    (G)et a Score
    (P)rint Result
    (S)how Star Rating
    (Q)uit"""
    print(menu)
    choice = input(">>>> ")
    score = -1
    while choice != "Q":
        choice = choice_check(choice)
        if choice == "G":
            score = input("Enter Score (0-100): ")
            score = score_check(score)
            print("Score Is Now", score)
            print(menu)
            choice = input(">>>> ")
        elif (choice in ("P", "S")) and int(score) not in range(0, 101):
            print("First Input A Score Value")
            print(menu)
            choice = input(">>>> ")
            choice = choice_check(choice)
        elif choice == "P" and int(score) in range(0, 101):
            print("{} is {}".format(score, users_score(score)))
            choice = input(">>>> ")
        elif choice == "S" and int(score) in range(0,101):
            print("*" * int(score))
            choice = input(">>>> ")
    print("Finished. Thank You")


def users_score(score):
    result = "Undecided"
    if int(score) < 0 or int(score) > 100:
        result = "Invalid score"
    elif int(score) >= 90:
        result = "Excellent"
    elif int(score) >= 50:
        result = "Passable"
    elif int(score) < 50:
        result = "Bad"
    return result


def choice_check(choice):
    menu = """    (G)et a Score
    (P)rint Result
    (S)how Star Rating
    (Q)uit"""
    options = ("G", "P", "S", "Q")
    if choice not in options:
        print("Invalid Choice")
        print(menu)
        choice = input(">>>> ")
        choice = choice_check(choice)
    return choice


def score_check(score):
    while True:
        try:
            0 > int(score)
        except ValueError:
            print("Input Is Not A Number")
            score = input("Enter Score (0-100): ")
            continue
        else:
            if int(score) not in range(0, 101):
                print("Not A Valid Input")
                score = input("Enter Score (0-100): ")
                score = score_check(score)
        return score


main()
