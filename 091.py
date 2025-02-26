# Father,Mother-> 5,5 from both

class Father:
    def father_moneys(self):
        return "5"

class Mother:
    def mommy_moneys(self):
        return "5"


class Child(Father,Mother):
    pass

son = Child()
print(son.father_moneys())
print(son.mommy_moneys())
