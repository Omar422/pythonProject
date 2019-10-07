# 49. Scope In Python p2

"""
# If you operate with the same variable name inside and outside of a function, Python will treat
  them as two separate variables, one available in the global scope (outside the function) and
  one available in the local scope (inside the function).

# If you need to create a global variable, but are stuck in the local scope, you can use
    the global keyword. The global keyword makes the variable global.
"""

x = 20
z = 5

def myFunc():
    x = 10
    global y
    y = 30
    z = 50

    print("The value of x inside the function= "+str(x))
    print("The value of z inside the function= "+str(z))

myFunc()
print("The value of x outside the function= "+str(x))
print("Access to the value of y outside the function = "+str(y))
print("The value of z outside the function= "+str(z))
