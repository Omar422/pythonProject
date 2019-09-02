# 14. List In python 2

"""
# Print part of list using index [2:5]
# Check if Item Exists. if "search" in list: do somthing
# Repeat item in list
"""



a = ["A", 4, "C", 2.5]
print("To print a part of list we use index, for ex: [1:3] index:3 won't be printting=> "+str(a[1:3]))

if "B" in a:
    print("Search for "B" in list a: Exist")
listp = ["python"] * 3
print(listp)
lists = a + listp
print(lists)
