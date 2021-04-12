a = int(input("enter the number"))
b = int(input("enter the number"))


def addition():
    return a+b


def subtraction():
    return a-b


def multiplication():
    return a*b


def division():
    return a/b


opretion = ['addition', 'subtraction', 'multiplication', 'division']

print("choose from following operation:"
      "addition,"
      "subtraction,"
      "multiplication,"
      "division")
o = input("enter the operation")

if o == opretion[0]:
    print(addition())
elif o == opretion[1]:
    print(subtraction())
elif o == opretion[2]:
    print(multiplication())
elif o == opretion[3]:
    print(division())
else:
    print("INVALID OPERATION")
