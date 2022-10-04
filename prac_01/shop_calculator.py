items = 0
total_cost = 0
while items <= 0:
    items = int(input("How Many Items Are There? "))
    if items <= 0:
        print("Invalid Input")
for i in range(1, items+1):
    item_cost = float(input("Please enter the Cost of Item {}: ".format(i)))
    total_cost = total_cost + item_cost
print("Total Cost of All Items is {}".format(total_cost))
