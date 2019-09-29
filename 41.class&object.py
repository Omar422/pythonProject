# 41. Classes And Objectss

"""
# Create Class using the keyword (class)
# Create object with assign it to the className(), cannot create object without class
# Note: The __init__() function is called automatically every time the class is being used to
create a new object.
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Omar", "23")
print(p1.name)
print(p1.age)
