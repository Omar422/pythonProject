# 59. Regular Expressions In Python p3

"""
# The sub() function replaces the matches with the text of your choice:
    # You can control the number of replacements by specifying the count parameter. sub('','',string,no)
# Match Object: A Match Object is as object containing information about the search and the result.
    The Match object has properties and methods used to retrieve information about the search,
        and the result. Ex: <re.Match object; span=(2, 4), match='is'>
    span() returns a tuple containing the start-, and end positions of the match.
    string returns the string passed into the function
    group() returns the part of the string where there was a match

"""

import re as myRegEx

str = "This Is His Issue"
match = myRegEx.sub('\s', '_', str, 2)

if (match):
    print('\nmatch')
    print(myRegEx.search('is',str))
    print(myRegEx.search(r"\bH+",str).span())
    print(myRegEx.search(r"\bH",str).string)
    print(myRegEx.search(r"\bH\w+",str).group())
