"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    score = float(input("Enter score: "))
    print(users_score(score))
    continue_result = input("Generate Random Score (Y/N)? ")
    while continue_result != "N" and continue_result != "Y":
        print("Invalid Input")
        continue_result = input("Generate Random Score (Y/N)? ")
    if continue_result != "N":
        score = random.randint(0, 100)
        print("The Random Score is", score)
        print("The Result is", users_score(score))
        print("Thank You.")
    else:
        print("Finished.")


def users_score(score):
    if score < 0 or score > 100:
        result = "Invalid score"
    elif score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    elif score < 50:
        result = "Bad"
    return result


main()
