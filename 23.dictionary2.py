# 22. Dictionaries In Python
"""
# To determine if a specified key is present in a dictionary use the in keyword.
# To determine how many items (key-value pairs) a dictionary has, use the len() method.
# Adding an item to the dictionary is done by using a new index key and assigning a value to it.
# The pop() method removes the item with the specified key name.
# The popitem() method removes the last inserted item.
# The del keyword removes the item with the specified key name.

"""

myd = {
    "name":"omar",
    "age": 23
}

if "age" in myd:
    print("check if there is a key with value \"age\"")
    print("Exist")
print("print the length of the dictionary with len() method= "+str(len(myd)))

print("\nthe main dictionary items are:\n"+str(myd))
myd["dob"] = 1996
print("Adding items to the dictionary, the new dictionary items are:\n"+str(myd))

myd.pop("age")
print("\nremove \"age\" using pop() method, the dictionary itmes are:\n"+str(myd))

myd.popitem()
print("\nremove last inserted item using popitem() method, the dictionary itmes are:\n"+str(myd))

myd["year"] = 2019
print("\nthe main dictionary items are:\n"+str(myd))
del myd["year"]
print("delete a specified item using its key name with del keyword, the dictionary itmes are:\n"+str(myd))

#del myd
#print("\nThis is will print an error")
#print(myd)
myd["age"] = 23
myd["dob"] = 1996
myd["year"] = 2019
print("\nthe main dictionary items are:\n"+str(myd))
myd.clear()
print("delete all items in the dictionary using clear() method, the dictionary items are:\n"+str(myd))
