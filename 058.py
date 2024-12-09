 # List
list1 = [45.4,56,78,965,324,]
print(len(list1))

# print unique Items
set1 =set(list1)
print(set1)


# Union - both of them
set1 = {4,7,5,6,9}
set2 = {5,6,2,7,8,2.5,87,.56}
my_set= set1.union(set2)
print(my_set)


#Common Value
set1 = {4,7,5,6,9}
set2 = {5,6,2,7,8,2.5,87,.56}
my_set= set1.intersection(set2)
print(my_set)

# Not included
set1 = {4,7,5,6,9}
set2 = {5,6,2,7,8,2.5,87,.56}
my_set= set1.difference(set2)
print(my_set)


set1 = {4,7,5,2,7,9,6,2,6,9}
set2 = {5,6,2}
subset = set2.issubset(set1)
print(subset)
