# name = input("What is your name? ")

# age = input("How old are you? ")

# city = input("Which city do you live in? ")

# print("Hello ", end="")
# print(f"{name}! You are {age} years old and live in {city}.")

# calculates the sum of three numbers given by the user

# sum = 0
# num1 = int(input("Enter the first number: "))
# sum += num1

# num2 = int(input("Enter the second number: "))
# sum += num2

# num3 = int(input("Enter the third number: "))
# sum += num3

# print(f"The sum of {num1} + {num2} + {num3} is:", sum)

# Write your solution here

# num1 = int(input("Enter first number:"))
# num2 = int(input("Enter second number:"))
# num3 = int(input("Enter third number:"))
# num4 = int(input("Enter fourth number:"))

# print(f"The sum of the numbers is {num1+num2+num3+num4} and the mean is {(num1+num2+num3+num4)/4}")

num = int(input("How many times a week do you eat at the student cafeteria?"))
price = float(input("The price of a typical student lunch? "))
groceries = float(input("How much money do you spend on groceries in a week? "))

print("Average food expenditure:")
print(f"Daily: {(num*price + groceries)/7} euros")
print(f"Weekly: {num*price + groceries} euros")