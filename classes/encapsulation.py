# public modifier    -> can be accessed by any derived class or same class
# class student:

#     def __init__(self):
#         self.name = 'Sam'     # default public attribute

#     def something (self):      # default public fn
#         pass



# private modifier.     __ can be accessed by same class only
# class student:

#     def __init__(self):
#         self.__name = 'Sam'     # __ (two underscore) default private attribute

#     def __something (self):      # __ (two underscore)  default private fn
#         pass



# protected modifier  _ can be accessed by same class or subclass
class student:

    def __init__(self):
        self._name = 'Sam'     # _ (one underscore)  default private attribute

    def _something (self):      # _ (one underscore)  default private fn
        pass



s = student()
print(s._name)