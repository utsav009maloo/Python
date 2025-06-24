# lst = []
# x = int(input("enter no."))
# for i in range(0,x):
#     ele = input()
#     lst.append(ele)
#     print(lst)

# def sort(lst,x):
#     for k in range(0,len(lst)):
#         for l in range(k + 1, len(lst)):
#             if lst[k] > lst[l]:
#                 lst[k],lst[l] = lst[l],lst[k]
#                 return lst

# ans = sort(lst,x)
# print("Soting element is: ", ans)


nums = [1, 2, 3, 2, 4]
dups = [x for x in set(nums) if nums.count(x) > 1]
print(dups)