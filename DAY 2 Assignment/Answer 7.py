#Write a program to accept a number from 1 to 12 and display name of the month and days in that month like 1 for January and number of days 31 and so on

A = int(input("Enter the number: -"))
if A == 1:
   print("January No.of days 31")
elif A == 2:
   print("February No.of days 28/29")
elif A == 3:
   print("March No.of days 31")
elif A == 4:
   print("April No.of days 30")
elif A == 5:
   print("May No.of days 31")
elif A == 6:
   print("June No.of days 30")
elif A == 7:
   print("July No.of days 31")
elif A == 8:
   print("August No.of days 31")
elif A == 9:
   print("September No.of days 30")
elif A == 10:
   print("October No.of days 31")
elif A == 11:
   print("November No.of days 30")
elif A == 12:
   print("December No.of days 31")
else:
   print("Please enter no. between 1 to 12")