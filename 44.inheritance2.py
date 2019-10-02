# 44. Inheritance 2

"""
# Python also have a super() function that will make the child class inherit all the methods and
    properties from its parent
    # By using the super() function, you do not have to use the name of the parent element, it will
        automatically inherit the methods and properties from its parent.
# If you add a method in the child class with the same name as a function in the parent class,
    the inheritance of the parent method will be overridden.
"""

class Person():
    def __init__(s, fname, lname):
        s.firstName = fname
        s.lastName = lname

    def printName(self):
        print(self.firstName, self.lastName)
    def printInfo(self):
        print(self.firstName, self.lastName,self.age)
p = Person("Omar", "Abdulaziz")
p.printName()

class Student(Person):
    def __init__(s, fname, lname, a):
        #Person.__init__(s, fname, lname)
        super().__init__(fname, lname)
        #s.age = 23
        s.age = a
    def printInfo(self): # Override the method in the parent class..
        print("Name:", self.firstName,self.lastName , ", Age:", self.age)
#Note: Use the pass keyword when you do not want to add any other properties or methods to the class.
    #pass
p1 = Student("Ali", "Hassan", 24)
p1.printInfo()
