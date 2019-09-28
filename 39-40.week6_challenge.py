# 39 - 40 : Sixth Week Challenge

week_challenge ="""
# Q1/ Use Recursion to print the result of 5^3 (5*5*5) \n
# Q2/ Create this list [-4, -6, -5, -1, 2, 3, 7, 9, 88], then print just the even numbers using lambda function
"""

print(week_challenge)
def power(N_base,N_power):
    if(N_power==1):
        return N_base
    else:
        return N_base*power(N_base,N_power-1)
print("Answer Q1:\n"+str(power(5,3)))

list = [-4, -6, -5, -1, 2, 3, 7, 9, 88]
print("Answer Q2:")
for x in list:
    if x > 0:
        evenN = lambda n : n
        print(evenN(x))
