# 22. Dictionaries In Python

"""
# {"key":"value"} , A dictionary is a collection which is unordered, changeable and indexed.
# to access the items we use its key name , inside square brackets [].
    # get() method that will give me the same result.
# to change the value of a specific item we use its key name.
# we can use a for loop, the return value are the keys of the dictionary, but there
    are methods to return the values as well using[]
# we can loop both keys and values, by using the items() function.
"""

myd = {
    "name":"omar",
    "age": 23
}

print("myd dictionary's values are: "+str(myd))
print("using the key age myd[\"age\"], the result is its value= "+str(myd["age"]))
print("using the get() method get.(\"age\"), the result is its value= "+str(myd.get("age")))

myd["age"] = 24
print("\nchange the age using its key myd[age]=24, the result after updating is= "+str(myd["age"]))

print("Using for loop, print(x), the keys: ....")
for x in myd:
    print(x)

print("Using for loop, print(myd[x]), the values: ....")
for x in myd:
    print(myd[x])

print("\nUsing for loop, for x in myd.vlaues() print the values: ....")
for x in myd.values():
    print(x)
print("print the values without using a for loop, myd.values() ...\n" + str(myd.values()))

print("\nUsing items() function with loop, the dictionary keys & values are: ")
for x,y in myd.items():
    print(x+":", y)
print("Using items() function without loop, the dictionary keys & values are:...\n" + str(myd.items()))
