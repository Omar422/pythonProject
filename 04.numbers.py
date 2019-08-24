# 04. numbers

####
# Python Numbers (Imtegers, Float, Complex)
###

x = 2
y = 4.0
z = 1j
print(type(x))
print(type(y))
print(type(z))
print("\n")
# Integers: positive or negative, without decimals, of unlimited length
x = 3
y = 465465944
z = -54665
print(type(x))
print(type(y))
print(type(z))
print("\n")

# Float: positive or negative, containing one or more decimals
x = 1.10
y = 5.0
z = -54665.2
print(type(x))
print(type(y))
print(type(z))
print("\n")

# Float can also be scientific numbers with an "e" to indicate the power of 10.
x = 35e3
y = 12e4
z = -87.7e100
print(type(x))
print(type(y))
print(type(z))
print("\n")

# Complex: with a "j" as the imaginary part
x = 3+5j
y = 5j
z = -5j
print(type(x))
print(type(y))
print(type(z))
print("\n")

# int(), float(), and complex() methods.
# You cannot convert complex numbers into another number type.
x = 2
y = 4.9
z = 1j
a = float(x)
b = int(y)
c = complex(x)
print(a)
print(b)
print(c)
print("\n")
print(type(a))
print(type(b))
print(type(c))

# Random Number In Python
"""Python does not have a random() function to make a random number, but
Python has a built-in module called random that can be used to make random numbers."""
import random
print(random.randrange(1,9))
print(random.randrange(1,9))
print(random.randrange(1,9))
print(random.randrange(1,9))
