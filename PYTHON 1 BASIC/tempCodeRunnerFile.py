#SET => It is immutable and not duplicate value allow.

my_set1 = {11,22,33,44,55,66}
print(my_set1)
my_set1.add(77)
print(my_set1)
my_set1.update([88,99],{100,101,102})
print(my_set1, end= "\n\n")

#the main diffrence of discard and remove ids in discard if no. not available it not show error but in remove it show error (KEYERROR)
my_set1.discard(88)
my_set1.remove(101)
print(my_set1, end= "\n\n")
my_set1.pop()
print(my_set1, end="\n\n")


#Union
my_set2 = {1,2,33,4,5,66,7,88,9}
print(my_set1 | my_set2)
print(my_set1.union(my_set2), end="\n\n")

#Intersection
print(my_set1 & my_set2)

print(my_set1 - my_set2)


for letter in set("HelloWorld !"):
    print(letter)


print(sorted(my_set1 | my_set2))

