# 03. variables

####
# Python has no command for declaring a variable
""" Variable names cannot start with a number,
    #it start with a letter (capital or small) or _ (underscore)
"""
# Variable names are case-sensitive which means (aA, Aa, AA, aa ) are four different vars
""" Python allows you to assign values to multiple variables in one line.
    And you can assign the same value to multiple variables in one line.
"""
####

x = 5
y = "hello, world!"
print(x)
print(y)

z = 2
z = "myText" # change vars' type & save the new value
print(z)

# "" = ''
a = 'omar'
b = "omar"
print(a)
print(b)

c, d, e = "Var c", "Var d", "var e"
print(c)
print(d)
print(e)

f = g = h = "3 variables have the same value"
print(f)
print(g)
print(h)

i = 'Python is'
print(i+' fun')

j, k = "Python is ", "easy"
print(j+k)

print(5+5)
print(5+"text")
