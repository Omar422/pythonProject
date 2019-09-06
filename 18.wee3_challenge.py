# 18. Week Three Test :

"""
Challenges:
    1- Create a list then use 4 of its function.
    2- Write a code to check if "python" exist in tuple = ("java", "python", "swift")
"""

list = ["python", "java"]
print("The main list has only two items, they're "+ str(list))
list.append("swift")
print("The new list after add item using append() " + str(list))
list.insert(0, "C++")
print("The new list after add item using insert() " + str(list))
list.pop()
print("The new list after remove last item using pop() " + str(list))
list.pop(0)
print("The new list after remove item in position [0] using pop() " + str(list))

tuple = ("java", "python", "swift")
if "python" in tuple:
    print("python is exist")
