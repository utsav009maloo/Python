#Array in Python
arr = [ "fight" , "Utsav" , "Moon"]
print(arr)

#Finding Length of array
new_arr = len(arr)
print(new_arr)

#Adding element in Array
arr.append("Night")
print(arr)

#Removing from array
arr.remove("Utsav")
print(arr)
del arr[1]
print(arr)
arr.pop(1)
print(arr)

#Modifiy elements using array
arr[0] = "Utsav"
print(arr)

#Repeat an array
a = ["why"]
a = a * 5
print(a)