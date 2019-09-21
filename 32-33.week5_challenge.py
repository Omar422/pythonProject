# Week Five Challenge

"""
# print every odd number in (A) from 3 to 17
# with every even number in (B) from 2 to 16
"""
"""for odd in range(3,17,2):
    for even in  range(2,16,2):
        print(str(odd) + " " + str(even))
"""
A = range(3,17,2)
B = range(2,16,2)

for odd in A:
    for even in B:
        print(str(odd)+" "+str(even))
    print("-----")
