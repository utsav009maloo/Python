lst = []
x = int(input("Enter the number of elements: "))
for i in range(0, x):
    ele = input()
    lst.append(ele)
    print(lst)


#Sorting in array
for k in range(0,len(lst)):
    for l in range(k + 1 , len(lst)):
        if lst[k] >= lst[l]:
            lst[k],lst[l] = lst[l],lst[k]

print(lst)