# 13. List In python

"""
# Lists can store different type of variables, other list
# to access the list items we use referring to the index number.
# to print the whole list we use for loop
"""



a = [1, "a", [1,"b"], 10.5]
print("This list has different type, to print the 3rd item a[2] => " + str(a[2]))
print("The items in a are: ")
for item in a:
    print item
numbers = [2, 6, 4.5, 8.75]
print("The items in number are: ")
for no in numbers:
    print no
numbers[2] = 4.25
print("the new value of numbers[2]= "+ str(numbers[2]))
del numbers[2]
print("the new list after delete numbers[2]= " + str(numbers))
del numbers # will delete the list
#print(numbers)
