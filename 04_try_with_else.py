

try:
    i = int(input("Enter number: "))
    c = 1/i
except Exception as e:
    print(e)
else:  # else executes when only try executes
    print("We wer successfull")
