# 15. List In python 3

"""
# List Methods
    len() the length of items
    append() add item to the list
    insert() add item in specific position
    remove() remove specified item
    pop() remove specified index, remove last item if index is not specified
    clear() remove all items

"""
print("Lesson 15: List Method")
list = ["apple", "banana", "cherry"]

list.append("orange")
list.append("blueberry")
print(list)
list.insert(0, "kiwi")
print(list)
list.remove("banana")
print(list)
list.pop()
print(list)
list.pop(3)
print(len(list))
print(list)
mylist = list.copy();
list.pop(2)
print(mylist)
print(list)
list2 = [1,2]

list.clear()
print(list)
