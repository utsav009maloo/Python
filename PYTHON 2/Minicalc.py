num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("1 for addition", "2 for subtraction", "3 for multiplication", "4 for division", sep="\n")
choice = int(input("Enter your choice: "))
if choice == 1:
    print(num1 + num2)
elif choice == 2:
    print(num1 - num2)
elif choice == 3:
    print(num1 * num2)
elif choice == 4:
    print(num1 / num2)
else:
    print("Invalid choice")
