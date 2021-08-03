# var :
#  global
#  local
a = 54  # global var


def func1():
    # a = 8  # local var
    global a
    print(a)
    a = 8
    print(a)


func1()
print(a)
