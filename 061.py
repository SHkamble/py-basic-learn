## tuple is immmutable in nature. Canot changed so can't get result


list1 = [10,20,30,40]
tuple1 = [10,20,30,40]
print(list1)
print(tuple1)


def mul_by_10(mylist):
    mylist[0]  *=10
    mylist[1]  *=10
    mylist[2]  *=10
    mylist[3]  *=10


print(list1)
mul_by10(list1)
mul_by10(tuple1)
print(list1)
print(tuple1)
