# 16. Tuple in Python

"""
# A tuple is a collection which is ordered and unchangeable.
# In Python tuples are written with round brackets ().
# if the tuple has just one item... ("item",)
# acces item in tuple with referring [index]
    # You cannot change its values. Tuples are unchangeable.
    # You cannot add items to it.
    # You cannot remove items in a tuple, but you can delete the tuple completely using del().
# You can loop through the tuple items by using a for loop.
"""
mixtuple = (1, "yellow", 0.1, "green")
print(mixtuple[1:3])
for item in mixtuple:
    print(item)
del mixtuple
print(mixtuple) # An error because it's no longer exist
