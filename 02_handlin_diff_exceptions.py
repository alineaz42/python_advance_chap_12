try:
    a = int(input("Enter a number: "))
    c = 1/a
    print(c)
except ValueError as e:
    print("Enter a valid value")
    print(e)
except TypeError as e:
    print("Exception occured 2")
    print(e)
except ZeroDivisionError as e:
    print("Make sure not dividing by zero")
    print(e)
except NameError as e:
    print("exception occured 4")
    print(e)
print("thanks using this code ")
