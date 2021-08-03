# types of error Zerodivision/NameError/SyntaxError..../memoryError
while True:
    print("enter q to quit the game")
    a = input("Enter a number: ")
    if a == 'q':
        break
    try:
        print("Trying....")
        a = int(a)
        if a > 6:
            print("You entered a number greater than six")
        else:
            print("you entered smaller than six")
    except Exception as e:
        print(f"Your input resulted in error{e} ")

print("Thanks playing this game")
