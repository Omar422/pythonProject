# 48. Scope In Python
"""
# A variable is only available from inside the region it is created. This is called scope.
➢ Local Scope
    A variable created inside a function belongs to the local scope of that function, and can only
        be used inside that function
➢ Global Scope
    A variable created in the main body of the Python code is a global variable and belongs to
        the global scope.
    Global variables are available from within any scope, global and local.
"""
y= 150
def myFucn():
    x = 300
    print("Access From myFucn, x= "+str(x))
    print("called Y -Global variable- from myFucn function, y= "+str(y))
    def myInnerFunc():
        print("Access From myInnerFunc, x= "+str(x))
    myInnerFunc()

#print(x) # Error
myFucn()
print("called Y -Global variable- from the main code, y= "+str(y))
