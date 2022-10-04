for i in range(1, 21, 2):
    print(i, end=' ')
print()
# a)
for i in range(0, 101, 10):
    print(i, end=' ')
print()
# b)
for i in range(20, 0, -1):
    print(i, end=' ')
print()
# c)
i = input("Number of Stars: ")
print("Here is {:.2f} Stars".format(int(i)))
while int(i) > 0:
    print("*", end=' ')
    i = int(i) - 1
print()
# d)
stars = int(input("Number of Star Rows: "))
for i in range(1, stars + 1):
    print('*' * i)
print()
