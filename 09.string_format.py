#09. Python Strings Format

a = """ 09_th Day: format()
    myText.format(myNumber1, myNumber2, myNumber3, ....)
    x.format(y) take the (x) and put it in the (y) where the brackets {} are.
    {index} => I can use it to be sure that it's in the correct place.
"""
t = "Hello world.. {1} ! I use Python version {0}"
n = 2
v = 3.7
print(a)
print(t.format(v,n))
