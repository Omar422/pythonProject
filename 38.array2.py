# 38. Array In Python
"""
# You can use the for in loop to loop through all the elements of an array.
# You can use the append() method to add an element to an array.
# You can use the pop() method to remove an element from the array.
# You can also use the remove() method to remove an element from the array.
"""

colors = ["red", "yellow", "green"]

print("The main items in the array are:")
for color in colors:
    print(color)

colors.append("black")
print("\nThe array after using append(\"black\"):\n"+str(colors))

colors.pop(0)
print("\nThe array after using pop(0):\n"+str(colors))

colors.remove("green")
print("\nThe array after using remove(\"green\"):\n"+str(colors))
