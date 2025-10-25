# # Write your solution here
# num = int(input("Please type in a number:"))
# if num == 1984:
#     print("Orwell")
# else:
#     exit()


name = input("Please tell me your name: ")

if name != "Jerry":
    qty = int(input("How many portions of soup? "))
    total = qty * 5.90
    print(f"The total cost is {total:.2f}")

print("Next please!")