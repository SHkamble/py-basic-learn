# Lambda function
"""def sayHello():
    print("Hello")
sayHello()


#new*
def funcWithParam(a):
    return a**2

o = funcWithParam(2)
print(o)
"""
# Lambda Expression --> Now copied by the Java

#def doubleOfme(value):
 #   return value*2

output = lambda value:value*2
print(output(3))

def sayHello(name):
    print("Hi your name is",name)

sayHelloLambda = lambda name: print("Hi your name is",name)
sayHello("Varsha")
sayHello("Sharda")