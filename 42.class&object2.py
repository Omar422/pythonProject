# 42. Classes And Objects

"""
# Objects can also contain methods. Methods in objects are functions that belong to the object.
# You can delete properties on objects by using the del keyword.
# You can delete objects by using the del keyword.

"""
class Person(object):
    def __init__(func, name, age):
        func.name = name
        func.age = age
# Note: The self parameter is a reference to the current instance of the class, and is used to
    # access variables that belong to the class.
    def myFunc(self):
        print("Hello my name is: "+self.name+"\nI'm "+str(self.age)+" years old.")

p1 = Person("Omar", "23")
p1.age = 24
p1.myFunc()
del p1.age
# p1.myFunc() => Error: AttributeError: 'Person' object has no attribute 'age'
del p1
# print(p1) => Error: NameError: name 'p1' is not defined
