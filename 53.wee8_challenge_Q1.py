# 53 . Week Eight Challenge

"""
# create a module have the basic calculation operations (+ - * /), Then apply:
    # 1+8
    # 4-2
    # 6*6
    # 8/2
"""

import calculationModule as op
from calculationModule import add as a
from calculationModule import sub as s
from calculationModule import mul as m
from calculationModule import div as d

print("1 + 8 = "+str(op.add(1,8)))
print("4 - 2 = "+str(op.sub(4,2)))
print("6 * 6 = "+str(op.mul(6,6)))
print("8 / 2 = "+str(op.div(8,2)))
print("-------------")
print("1 + 8 = "+str(a(1,8)))
print("4 - 2 = "+str(s(4,2)))
print("6 * 6 = "+str(m(6,6)))
print("8 / 2 = "+str(d(8,2)))
