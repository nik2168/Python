# class attribute:
# defined in a class blueprint, and are same for all the objects

# instance attribute:
# defined for any particular object & can be accessed by that object only

class animal:

    info = 'this is a animal class'    # class attribute

    def __init__(self, name):
        self.name = name


a = animal("Cat")
print(a.name)     # class attribute, aleady defined in class
a.age = 12        # instance attribute

print(a.age)
animal.info = "changed the animal info !"  # can change the class attribute by class name
print(a.info)