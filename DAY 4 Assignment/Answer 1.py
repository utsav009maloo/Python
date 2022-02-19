#Python program to print Highest Common Factor (HCF) of two numbers.

x = 20
y = 50
if x > y:
  x, y = y, x
for i in range(1,x+1):
  if x%i == 0 and y%i == 0:
    hcf = i
print("HCF of", x, "and", y, "is:", hcf)