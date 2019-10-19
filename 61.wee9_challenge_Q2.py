# 61 . Week Challenge Q2

"""
# Use RegEx (Regular Expression) to find word (data) in this sentence (data is the new oil)
"""

import re as RegEx

str = 'data is the new oil'
print(RegEx.findall('data', str))
print(RegEx.search('data', str))
