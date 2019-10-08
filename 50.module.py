# 50 . Module In Python

"""
# module: A file containing a set of functions you want to include in your application.
# To create a module just save the code you want in a file with the file extension .py
# We can use the module by using the import statement.
# Note: When using a function from a module, use the syntax: module_name.function_name.
# The module can contain variables of all types (arrays, dictionaries, objects etc).
#
"""
import mymodule

# module_name.function_name.
mymodule.greeting("Omar")

print("name:",mymodule.person["name"],
        ", age:",mymodule.person["age"],
        ", country:", mymodule.person["country"])
