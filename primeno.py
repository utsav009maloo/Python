num = int(input("Enter a number: "))
if num == 1:
    print("1 is neither prime nor composite")
if num >= 2:
    for i in range(2, num):
        if num % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")
