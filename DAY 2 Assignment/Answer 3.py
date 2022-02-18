#Write a program to check whether a person is eligible for voting or not. (accept age from user)

Me = int(input("Enter age: "))
if Me >= 18:
    print("Eligible for voting: ", Me)
else:
    print("Not eligible for voting: ", Me)