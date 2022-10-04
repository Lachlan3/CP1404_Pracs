"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        bonus = sales * 0.1
        print("Bonus is: $", bonus)
        sales = float(input("Enter sales: $"))
    elif sales > 1000 or sales == 1000:
        bonus = sales * 0.15
        print("Bonus is: $", bonus)
        sales = float(input("Enter sales: $"))
    # I added a feature to ask the user if they want to continue or not as well
    repeat = input("Restart? Y or N: ")
    if repeat == "Y":
        sales = float(input("Enter sales: $"))
    elif repeat == "N":
        sales = -1
    else:
        print("Invalid Input")
        sales = -1
print("Invalid Value, Thank You")
