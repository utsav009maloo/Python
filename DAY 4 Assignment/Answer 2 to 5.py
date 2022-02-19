# Question 2. What will be the output of the following Python code?
i=0
def change(i):
   i=i+1
   return i
change(1)
print(i)

#Answer :- Option[c]=0


# Question 3. What will be the output of the following Python code?
def a(b):
    b = b + [5]
 
c = [1, 2, 3, 4]
a(c)
print(len(c))

#Answer :- Output is 4.


# Question 4. What will be the output of the following Python code?
a=10
b=20
def change():
    global b
    a=45
    b=56
change()
print(a)
print(b)

#Answer :- Option[a]=10 , 56.


# Question What will be the output of the following Python code?
def change(i = 1, j = 2):
    i = i + j
    j = j + 1
    print(i, j)
change(j = 1, i = 2)

#Answer :- Option[d]=3 , 2.