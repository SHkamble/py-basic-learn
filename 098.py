a = int(input("Enter your A number"))
b = int(input("Enter your B number"))
try:
    c = a/b
    print(c)
except Exception as error:
       print("You are dividing the vallue of A with Zero. Please don't do it", error)

