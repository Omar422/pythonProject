# 29. For Loop In Python

"""
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set,
or a string). This is less like the for keyword in other programming languages and works more
like an iterator method as found in other object-orientated programming languages.
With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc
# Even strings are iterable objects, they contain a sequence of characters.
# With the break statement we can stop the loop before it has looped through all the items.
"""

for l in "AB":
    print(l)

names= ["omar", "ahmed", "ali", "aymen"]
for name in names:
    # Exit the loop when x is "ali", but this time the break comes before the print.
    # if name == "ali":
        # break
    if name == "ahmed":
        continue
    print(name)
    if name == "ali":
        break
