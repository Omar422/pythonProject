# 45 . Iterators In Python
"""
# An iterator is an object that contains a countable number of values.
# Technically, in Python, an iterator is an object which implements the iterator protocol,
    which consist of the methods __iter__() and __next__()
        To create an object/class as an iterator you have to implement the
            methods __iter__() and __next__() to your object.
# Even strings are iterable objects, and can return an iterator.
#
"""

mytuple = ("One", "Two", "Three")
myit = iter(mytuple)
print("\n"+next(myit),"\n"+next(myit),"\n"+next(myit))
"""print(next(myit))
print(next(myit))
print(next(myit))
"""
print("------------------")

s = "String"
# The for loop actually creates an iterator object and executes the next() method for each loop.
for mys in s:
    print(mys)
print("------------------")
class myNumber:
    def __iter__(self):
        self.a = 1 # init value
        return self
    def __next__(self):
        if self.a <=20:
            x = self.a
            self.a += 1
            return x
        else:
            # To prevent the iteration to go on forever, we can use
                # the StopIteration statement.
            raise StopIteration

obj = myNumber()
myiter = iter(obj)

for x in myiter:
    print(x)
