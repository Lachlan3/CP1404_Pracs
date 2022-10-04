# get name
# display menu
# get choice
# while choice != Q
#    if choice == H
#        display "hello" name
#    else if choice == G
#        display "goodbye" name
#    else
#        display invalid message
#    display menu
#    get choice
# display finished message
name = input("Enter Name: ")
menu = """(H)ello
(G)oodbye
(Q)uit"""
print(menu)
choice = input(">>> ")
while choice != "Q":
    if choice == "H":
        print("Hello {} \n".format(name))
    elif choice == "G":
        print("Goodbye {} \n".format(name))
    else:
        print("Invalid Input \n")
    print(menu)
    choice = input(">>> ")
print("Finished.")
