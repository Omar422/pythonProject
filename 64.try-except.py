# 64 . Try-Except In Python

"""
# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.
# When an error occurs, or exception as we call it, Python will normally stop and generate an
    error message. These exceptions can be handled using the try statement
# You can define as many exception blocks as you want, if you want to execute a special
    block of code for a special kind of error
# You can use the else keyword to define a block of code to be executed if no errors were raised.
# The finally block, if specified, will be executed regardless if the try block raises
    an error or not.
"""
x = 10
try:
    print(x)
except NameError:
    print('Variable x isn\'t defined')
except Exception as e:
    e = 'an exception occured'
    print(e)
else:
    print('no errors were raised')
finally:
    print('Done')
