# 17. Tuple in Python 2

"""
# To determine if a specified item is present in a tuple use the in keyword.
# To determine how many items a tuple has, use the len() method.

"""
mixtuple = (1, "yellow", 0.1, "green")
print(mixtuple[1:3])
if "yellow" in mixtuple:
    print("Exist")
python = ("python",) *3
print(python)
new = mixtuple + python
print(new)

x = (1,2,3,4)
x = x + (5,6,7)
print(x)
print(len(x))

mytuple = tuple(("a", "b", "c", "d"))
print(mytuple)
ftuple = [1, "o", 4, "m"]
ttuple = tuple(ftuple)
print(ttuple)
