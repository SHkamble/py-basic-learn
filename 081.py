class person:

    def __init__(self,name):
      self.name = name
    print("You created an object")

    def printDetails(self):

        print("Your details are",self.name)


    def printDetails2(self):
        print("Your details are",self.name)

amit = person("amit")
amit.printDetails2()

nikhil = person("nikhil")
nikhil.printDetails2()