# 36. Lambda Function In Python P2
"""
# The power of lambda is better shown when you use them as an anonymous function inside another function
#
"""

def myFunc(n):
    return lambda a : a * n
doubler = myFunc(2) # value of n
tripler = myFunc(3) # value of n
print("The power of lambda is better shown when you use them as an anonymous function inside")
print(doubler(11)) # value of a
print(tripler(11)) # value of a
