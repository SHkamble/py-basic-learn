# multilevel Inheritance
# Level - GF -> F -> son


class GrandFather:
    def grandFather_method(self):
        return "GrandFather Method"


class Father(GrandFather):
    def father_method(self):
        return "Father Method"

class Son(Father):
    def son_method(self):
        return "Son Method"


son = Son()
print(son.son_method())
print(son.father_method())
print(son.grandFather_method())