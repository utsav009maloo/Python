import random
list1 = [1,2,3,4,5]
print(random.choice(list1))
print(random.random())
print(random.uniform(1,10))
print(random.randrange(1,10))
print(random.randrange(1,10,2))
print(random.randint(1,10))
random.shuffle(list1)
print(list1)