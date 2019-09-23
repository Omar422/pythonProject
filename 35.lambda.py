# 35. Function Lambda
"""
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments but can only have one expression.
# Syntax For Lambda:
    lambda arguments: expression
"""
# we need to assign lambda to a variable so we can call it using variable name
x = lambda x: x + 10
print("lambda add the argument to 10.. x(5)\n"+str(x(5)))

x = lambda x,y : x * y
print("\ncall lambda function which was stored in variable x, it multiplies the arguments.. x(5,6)\n"+str(x(5,6)))
