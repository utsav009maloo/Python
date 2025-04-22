def largest(lst,x):
    y = lst[0]
    for i in range(1, x):
        if lst[i] > y:
            y = lst[i]
            return y
lst = []
x = int(input("Enter the number of elements: "))
for i in range(0, x):
    ele = int(input())
    lst.append(ele)
    print(lst)
    
ans = largest(lst,x)
print("Largest element is: ", ans)
