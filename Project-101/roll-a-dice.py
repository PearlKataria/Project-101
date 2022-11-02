import random
response="y"

while response == "y":
    no = random.randint(1,6)
    if(no == 1):
        print("The dice has rolled to 1 *")
    elif(no == 2):
        print("The dice has rolled to 2 **")
    elif(no == 3):
        print("The dice has rolled to 3 ***")
    elif(no == 4):
        print("The dice has rolled to 4 ****")
    elif(no == 5):
        print("The dice has rolled to 5 *****")
    else:
        print("The dice has rolled to 6 ******")
    response=input("press y to roll again and n to exit: ")
