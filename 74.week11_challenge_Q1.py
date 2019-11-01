# 74. Week Challenge Q1
"""
text.file:
    What is Python language?
    Python is a widely used high-level, general-purpose, interpreted, dynamic programming language.
    Its design philosophy emphasizes code readability, and its syntax allows programmers to express
    concepts in fewer lines of code than possible in language such as C++ or Java.
    Python supports multiple programming paradigms, including object-oriented, imperative and
    functional programming or procedural styles. It features a dynamic type system and automatic
    memory management and has a large and comprehensive standard library.
# add the content ( The best way we learn anything is by practice and exercise questions ) to the text.file
"""

file = open('text.txt')
print("------------\nMain Content: "+file.read())
file.close()

file = open('text.txt', 'a')
file.write('The best way we learn anything is by practice and exercise questions')
file.close()

file = open('text.txt')
print("------------\nAfter Append: "+file.read())
file.close()
