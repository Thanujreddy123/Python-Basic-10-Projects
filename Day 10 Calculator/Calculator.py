def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


flag = True
while flag:
    print("This is a calculator")
    print(" There are four operations: +, -, *, /")
    print("There are two numbers: a and b ")
    a = int(input("enter first number:"))
    b = int(input("enter second number:"))
    operation = input("enter operation:->")
    dictoperator = {"+": add, "-": sub, "*": multiply, "/": divide}
    function = dictoperator[operation]
    print(function(a, b))
    status = input("enter the yes to no to exit")
    if status == "no":
        flag = False
