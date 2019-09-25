# 37 Array In Python

"""
# Arrays are used to store multiple values in one single variable.
# You refer to an array element by referring to the index number.
"""

color = ["red", "yellow", "green"]

print("Array:\n"+str(color))

print("\nthe first item (means index[0]):\n"+color[0])

color[1] = "blue"
print("\nAfter update the second item:\n"+str(color))

# The length of an array is always one more than the highest array index
print("\nThe length of the array using len():\n"+str(len(color))+"\n")
