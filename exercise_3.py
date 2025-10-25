# Calculator
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

Operation = input("Enter the operation: add, subtract, multiply: ")

if Operation == "add":
    print(f"{num1} + {num2} = {num1 + num2}")

elif Operation == "subtract":
    print(f"{num1} - {num2} = {num1 - num2}")  

elif Operation == "multiply":
    print(f"{num1} * {num2} = {num1 * num2}")

