# 20. Sets In Python

"""
# A set is a collection which is unordered and unindexed.
# In Python sets are written with curly brackets {}.
# A Set doesn't store the value more than once.
# You cannot access items in a set by referring to an index.
# you cannot change set items, but you can add new items.
# add one item with add() method.
# add more than one item with update([]) method.
"""

set = {"one", 1, "two", "three", 1}
print(set)
print("Using For and in: ")
for s in set:
    print(s)
print("one" in set)
set.add("four")
set.update(["five","six"])
print(set)
