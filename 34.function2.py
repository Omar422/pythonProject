# 34. Function In python Part 2

"""
# You can send any data types of parameter to a function (string, number, list, dictionary etc.)
# To let a function, return a value, use the return statement.
# You can also send arguments with the key = value syntax.
    This way the order of the arguments does not matter
# add a * before the parameter name in the function definition
    will receive a tuple of arguments and can access the items accordingly
"""
print("\nArgument list")
def myFunc(food):
    for x in food:
        print(x)
eat = ["apple", "banana"]
myFunc(eat)


print("\nsend arguments with the key = value syntax")
def arg(a,b,c):
    print("value of argument b is: "+b)
arg(a="first", c="second", b="third")


print("\nadd a * before the parameter name to make a tuple of arguments")
def argumentTuple(*numbers):
    print("print element in position 4, numbers[4]: "+numbers[4])
argumentTuple("one","two","three","four","five")


print("\nAn example to use recursion")
def tryrecursion(k):
    if(k>0):
        result = k + tryrecursion(k-1)
        print(result)
    else:
        result = 0
    return result
tryrecursion(6)
