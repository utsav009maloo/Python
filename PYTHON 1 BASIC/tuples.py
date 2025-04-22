# #We can not change elements of Tuples.
# #tuples are immutable
tuple1 = ()
print(tuple1)

tuple2 = (1,2,3,74)
print(tuple2)

tuple3 = ("Utsav" , 101 , 7 , "Maloo")
print(tuple3)

tuple4 = ("LIST", "Tuple", [1,2,3,4],(4,3,2,1))
print (tuple4)

tuple5 = "LIST", "Tuple", [1,2,3,4],(4,3,2,1)
print (tuple5)

tuple6 = 9,"UTSAVMALOO",8,7,6,5,4,[3,2,1]
print(tuple6)
print(tuple6[2])
print(tuple6[1][5])
print(tuple6[7][2])


#Slicing
tuple7 = 'a','s','d','f','g','g','h','j'
print (tuple7[1:3])
print (tuple7[:-3])
print (tuple7.count('g'))
print (tuple7.index('d'))