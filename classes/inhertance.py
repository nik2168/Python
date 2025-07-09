
class Parent:
    info = "Parent class info"
    pass

class child(Parent):
    info = "Child class info"
    pass

a = child()
print(a.info)