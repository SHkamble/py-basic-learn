# Identity Operator:
# in returns true if both valariables are same object
# is not returns true if both variables are not the same objet
# "is" used when we writr list, set , dictionary.
# primitive (means no list , set, dict) never user used "is"

x = [1 ,2 ,3 ]
y = [1 ,2 ,3 ]

print(x is y)
print(id(x ))
print(id(y ))

print(x is y)
print(x is not y)
print(id(x))
print(id(y))




































