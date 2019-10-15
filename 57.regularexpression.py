# Regular Expressions In Python

"""
# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
# RegEx can be used to check if a string contains the specified search pattern.
# Python has a built-in package called re, which can be used to work with Regular Expressions.
    # When you have imported the re module, you can start using regular expressions:
#
"""

import re

txt = "This Is My First1 Training, 22 This Is Python3 RegEx"

check = re.search("^This.*RegEx$",txt)
if (check):
    print("match")
    print(re.split('Is|This', txt))
    print(re.findall('This', txt))
    print(re.sub('My', 'Our', txt))

    print(re.findall('\d', txt))
    print(re.findall('\W', txt))

    print(re.findall('[Ex]', txt))
    print(re.findall('[^0-9]+', txt))
    print(re.findall('[^a-zA-Z]+', txt))
else:
    print("no match")
