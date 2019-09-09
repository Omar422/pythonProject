# 21. Sets In Python 2

"""
# len() to know how many itmes in the set.
# To remove an item in a set, use the remove(), or the discard() method.
    # remove() => will raise an error if doesn't find the item
    # discard() => won't raise an error if doesn't find the item
# pop() remove random item
# clear() delete all itmes
# del() delete the set completely.
# the set() constructor is use to make a set.
"""

set = {"one", 1, "two", "three", 10}
set.remove(10)
set.discard(1)
pop = set.pop()
set.clear()

print("The deleted item is: "+pop)
print("The lenght of the set= "+str(len(set)))
print("The set after using clear() method is= "+str(set))

set2 = (1,2)
del set2
#print(set2)

#myset = set(("first", "second"))
#print(myset)
