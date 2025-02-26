# Single Inheritance - 90%
# Us the properties,variable and, methods of your base class or parent class by the sub classs or son class.

class Father :
    bank_bal = 100000000000


    def one_bhk(self):
        print("Use it son")


class Son (Father) :
    pass  # I will write code in future , skip!!!

s = Son()
s.one_bhk()
print(s.bank_bal)
