#tuple creation
tuple1 =   ()
tuple2 = (1,2,3,4,5,6)
tuple3 = tuple(["sharda","Varsha"])
print(tuple1)
print(tuple2)
print(tuple3)

# Merging of tuples
hero1 = ("sharukh","salman")
hero2 = ("Wonder woman","sharad kelkar")
awesome_team = hero1 + hero2
print(awesome_team)


# Convert to list
my_tuple = (1,2,3,4,5,)
print(list(my_tuple))


# this is multiple value assigned.
x = 10
a,b = 23,45  #this is multiple value assigned.
q ,w, r = 49,78,65  # tuple assigned to multiple variables.
print(q)
print(w)
print(r)

# Nested tuples
hero1 = ("sharukh","salman")
hero2 = ("Wonder woman","sharad kelkar")
awesome_team = hero1, hero2
print(awesome_team)
print(awesome_team[0])
print(awesome_team[1][1])

print(awesome_team[0][1])

# Search in tuple
cities = ("Mumbai","Paris","kedarnath","ujjain","kerla")
print("Paris" in cities)
print("singapore" in cities)

