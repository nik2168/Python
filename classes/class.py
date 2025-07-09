
class student:

    def __init__(self, name):
        self.name = name
        pass # pass is used as null or doing nothing for some fn, statement or constructor 

    def const (self, name, age, rollno):
        self.name = name
        self.age = age
        self.rollno = rollno

    def getInfo (self):
        print(self.name, self.age, self.rollno)

    def getName (self):
        print(self.name)



s1 = student("Nik")
s1.getName()

s2 = student("Nik")
s2.const("Nik", 20, 1)
s2.getInfo()