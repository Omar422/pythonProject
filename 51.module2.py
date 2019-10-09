# 51 . Module In Python p2

"""
# You can create an alias when you import a module, by using the as keyword.
# There are several built-in modules in Python, which you can import whenever you like.
# There is a built-in function to list all the function names (or variable names) in a module. dir()
# You can choose to import only parts from a module, by using the from keyword.
"""
import platform
import mymodule as md
from mymodule import person
# Import and use the platform module. (built-in modules)


print("my name is "+md.person["name"])
print("my name is "+person["name"])
print("platform.system(): "+platform.system())
print("platform.python_version(): "+platform.python_version())

# Note: The dir() function can be used on all modules, also the ones you create yourself.
for x in dir(md):
    print(x)

#print(dir(platform))
print(dir(platform))
