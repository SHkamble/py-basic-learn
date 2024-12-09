# MAp and Filter in the list

sq = lambda x : x*x
result = sq(5)
print(result)


  # Map function ( where we will go from one item and apply a functions)
numbers= [1,2,3,4,5,]

sq_numbers = []
for i in numbers:
    sq_numbers.append(sq(i))
print(sq_numbers)

def  triple(a):
      return a * 3  #a**3 write for cube



# map function
sq_numbers3 =list (map(lambda x : x*3,numbers))
sq_numbers2 =list (map(lambda x : x*x,numbers))
print(sq_numbers2)
print(sq_numbers3)

sq_numbers2 =list (map(triple,numbers))
print(sq_numbers2)