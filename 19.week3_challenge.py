# 18. Week Three Test :

"""
Challenges:
    1- Create a list then use 4 of its function.
    2- Write a code to check if "python" exist in tuple = ("java", "python", "swift")
"""

list = ["python", "java"]
print("The main list has only two items, they're "+ str(list))
newlist = list.copy()
print("The copied list after using copy() "+ str(newlist))
newlist.extend(list)
print("The new list after using extend() "+ str(newlist))
newlist.remove("python")
print("The new list after remove item using remove() " + str(newlist))
newlist.sort()
print("The new list after using sort() "+str(newlist))

tuple = ("java", "python", "swift")
if "python" in tuple:
    print("python is exist")
