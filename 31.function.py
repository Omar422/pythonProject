# 31. Functions In Python
"""
# A function is a block of code which only runs when it is called. You can pass data, known as
    parameters, into a function. A function can return data as a result.

# Information can be passed to functions as parameter.
    Parameters are specified after the function name, inside the parentheses. You can add as many
    parameters as you want, just separate them with a comma.
"""

def my_function(fname = "Omar"):
    print("My First Name is: "+fname)

# To call a function, use the function name followed by parenthesis
my_function() # Default = Omar
my_function("Ali")
