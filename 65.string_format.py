#65. Python Strings Formatting

"""
# To make sure a string will display as expected, we can format the result with
    the format() method.
# The format() method allows you to format selected parts of a string.
    #Sometimes there are parts of a text that you do not control, maybe they come from a database,
    or user input? .To control such values, add placeholders (curly brackets {}) in the text, and run
    values through the format() method.
# If you want to use more values, just add more values to the format() method.
#
"""

name = "ali"
age = 25
salary = 100
stmt = "Name: {}\nAge: {}\nSalary: {:.2f} dollars"
print(stmt.format(name,age,salary))
