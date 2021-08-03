a = [1, 2, 4, 5, 7, 8, 9, 5, 4, 8, 4, 2]
b = []
for item in a:
    if item % 2 == 0:
        b.append(item)
print(b)

# shortcut for above code
b = [i for i in a if i % 2 == 0]  # used in most cases
c = {i for i in a if i % 2 != 0}  # set comprehension
print(c)
print(b)
