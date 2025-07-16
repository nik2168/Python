a = int(input("Enter number a : "))
b = int(input("Enter number b : "))

try:
    result = a / b
except ZeroDivisionError:
    result = None
    print("can't divide by zero !")
finally:
    print("Result : ", result)