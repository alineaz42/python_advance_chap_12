# sklearn search for different errors

def increment(num):
    try:
        return int(num)+1
    except:
        raise ValueError("This is not good ")


# a = increment("dfd") # will throw error
b = increment(5)
print(b)
