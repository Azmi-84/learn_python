def add_numbers(num1, num2):
    result = num1 + num2
    return result


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = add_numbers(num1, num2)
print("The addition of", num1, "and", num2, "is", result)
