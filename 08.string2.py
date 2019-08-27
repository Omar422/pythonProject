#08. Python Strings2

string = """
"8th_Day: Python Strings 2
\nThere are many functions to use with strings:
string.strip()                  => Deletes space from beginning or end of the string.
len(string)                     => Returns the length of a string
string.lower()                  => Returns the string in lower case
string.upper()                  => Returns the string in upper case
string.replace("old","new")     => Replaces a string with another one"
string.split("x")               => Splits the strings into substring if find x"
"""

print(string)
testString = "  This Is A string..!   "
print("strip()  => " + testString.strip())
print("len()    => " + str(len(testString)))
print("lower()  => " + testString.lower())
print("upper()  => " + testString.upper())
print("replace()=> " + testString.replace("A","My"))
print(testString.strip().split(" "))
