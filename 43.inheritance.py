# 43. Inheritance

"""
# Inheritance allows us to define a class that inherits all the methods and properties from
    another class.
# To create a class that inherits the functionality from another class, send the parent class as a
    parameter when creating the child class.
# When you add the __init__() function, the child class will no longer inherit the parent's
    __init__() function.
# Note: The child's __init__() function overrides the inheritance of the
    parent's __init__() function.
# To keep the inheritance of the parent's __init__() function, add a call to the parent's
    __init__() function: parent.__init__(...,...,..)
"""

class Person():
    def __init__(s, fname, lname):
        s.firstName = fname
        s.lastName = lname

    def printName(self):
        print(self.firstName, self.lastName)
p = Person("Omar", "Abdulaziz")
p.printName()

class Student(Person):
    def __init__(s, fname, lname):
        Person.__init__(s, fname, lname)
#Note: Use the pass keyword when you do not want to add any other properties or methods to the class.
    #pass
p1 = Student("Ali", "Hassan")
p1.printName()
