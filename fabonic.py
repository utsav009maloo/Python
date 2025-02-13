"""def s(n):
    if n <= 1:
        return n
    else:
        return(s(n-1) + s(n-2))
y = int(input())
if y <= 0:
    print("Plese enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(y):
        print(s(i))"""

a = 0
b = 1
num = int(input("Enter the value of 'n': "))
if num == 1:
    print(a)
else:
    print(a)
    print(b)
    for i in range(2, num):
        c = a + b
        a = b
        b = c
        print(c)