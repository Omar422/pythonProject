# 30. For Loop In Python range()

"""
# To loop through a set of code a specified number of times, we can use the range() function,
    The range() function returns a sequence of numbers, starting from 0 by default, and
    increments by 1 (by default), and ends at a specified number.
# The range() function defaults to 0 as a starting value, however it is possible to specify the
    starting value by adding a parameter: range(2, 6), which means values from 2 to 6
    (but not including 6)
# The range() function defaults to increment the sequence by 1, however it is possible to
    specify the increment value by adding a third parameter: range(2, 30, 3)
# The else keyword in a for loop specifies a block of code to be executed
    when the loop is finished
"""
print("""
range(10,100,10)\n
    the first value'10' where to start, it's = 0 by default\n
    the second value'100' is the end value 'not including it'\n
    the third value'10' is the increments value\n
""")
for l in range(10, 100, 10):
    print(l)
else:
    print("Else in for loop is working when loop is finished")
a = ["red", "blue", "orange"]
b = ["shirt", "hat", "shoes"]
an = ["a", "e", "i", "o", "u"]
s = "a "
for x in a:
    for y in b:
        if x[0] in an:
            s = "an "
        print(s+x,y)
