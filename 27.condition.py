# Conditional Statements In Python
    # if ... elif ... else
"""
# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b
"""

a= 25;
b= 50;
c= 75;
print("The values are: a= "+str(a)+", b="+str(b)+", c="+str(c))
print("if a > b print 'a is bigger than b'\nelif a < b print 'b is bigger than a'\nelse print 'they are equals'")
if a > b:
    print("a is bigger than b")
elif a < b:
    print("b is bigger than a")
else:
    print("they are equals")

print("\nNested if.....")
if c > a:
    print("c is bigger than a")
    if c > b:
        print("c is also bigger than b")
else:
    print("c isn't bigger than a")


print("\nOperator and & or with one line conditions .....")
print("b isn't the smallest value") if b > a or b > c else print("a is the highest value") if a > b and a > c else ".."
