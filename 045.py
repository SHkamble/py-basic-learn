"""digit = 12345
mod1 = digit%10
print(mod1)
digit=12345
mod2 = digit%10
print(mod2)
digit=1234
mod3 = digit%10
print(mod3)
digit=123
mod4 = digit%10
print(mod4)
digit=12
mod5 = digit%10
print(mod5)
digit=1
mod6 = digit%10
print(mod6)
print(mod1+mod2+mod3+mod4+mod5+mod6)
"""

num = int(input("Enter the number\n"))
sum=0
while num!=0:
    digit = num%10
    sum = sum+digit
    num //=10     # num= int(num/10)
print(sum)