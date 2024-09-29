name = str(input("Enter your name: "))
age = int(input("Enter your age: "))

if name == "azmi" and age == 84:
    print("hello azmi and age is 84")
else:
    print("wrong name or age")

#  maiking a calaulator

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print(num1, "is greater than", num2)
else:
    print(num2, "is greater than", num1)

operation = str(input("Enter operation: "))

if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1 * num2)
elif operation == "/":
    print(num1 / num2)
else:
    print("wrong operation")
