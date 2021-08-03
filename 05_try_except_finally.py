try:
    i = int(input("Enter number: "))
    c = 1/i
except Exception as e:
    print(e)
    exit()
finally:  # will must run though the programs stops
    print("We are done")

print("thanks for using the program")
