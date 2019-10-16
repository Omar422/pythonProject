# 58. Regular Expressions In Python p2

"""
# The findall() function returns a list containing all matches.
# The search() function searches the string for a match, and returns a Match object if there is a match.
    # If there is more than one match, only the first occurrence of the match will be returned
# The split() function returns a list where the string has been split at each match:
"""

import re as myRegEx

str = "This is his issue"
match = myRegEx.findall('is', str)

if (match):
    print(match)
    if (myRegEx.findall('ab', str)) :
        print('match')
    else:
        print('No match\n')

s = myRegEx.search("\s", str)
ns = myRegEx.search('ab', str)
if (s):
    print(s.start())
    print(ns)

s = myRegEx.split("\s", str)
print('\n',s)
