#11. Python Operators Part2

a = """ 11_th Day: Operators (7 groups)
    4- Logical: ( and , or , not )
    5- Identity: ( is , is not )
        ** used to compare the objects and know if they have the same location.
    6- Membership: ( in , not in )
        **  test if a sequence is presented in an object.
    7- Bitwise: ( & , | , ^ , ~ , << , >>)
        **  compare (binary) numbers.
"""
x = 10
y = 11
z = ['python', 'C++']
print(not(x > 10 or x < 10))
print(x is not y)
print('C#' not in z)
