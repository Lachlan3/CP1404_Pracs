import random
# Some Concepts found @ https://www.pythontutorial.net/python-basics/python-write-text-file


def main():

    number_of_scores = input("Input the Number of Desired Random Scores (0-100) >>> ")
    while not 0 < int(number_of_scores) < 100:
        print("Invalid Input")
        number_of_scores = input("Input the Number of Desired Random Scores (0-100) >>> ")
    with open("results.txt", "w") as f:
        for i in range(0, int(number_of_scores)):
            score = random.randint(0, 100)
            line = "{} is {} \n".format(score, users_score(score))
            f.write(line)


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
