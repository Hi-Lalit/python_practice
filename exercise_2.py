# Ask the user for a number
number = int(input("Please type in a number: "))

# Check the magnitude of the number
if number < 1000:
    print("This number is smaller than 1000")
    if number < 100:
        print("This number is smaller than 100")

print("Thank you!")
