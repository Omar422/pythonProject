# 66. Python Strings Formatting p2

"""
# You can use index numbers (a number inside the curly brackets {0}) to be sure the values are
    placed in the correct placeholders.
# You can also use named indexes by entering a name inside the curly brackets {carname}, but
    then you must use names when you pass the parameter values
"""

q,i,p = 3,9,6

stmt = "q= {0}\np= {2}\ni= {1:.1f}\np+q= {1:.1f}".format(q,i,p)
stmt2 = "q= {q_value}\np= {p_value}\ni= {i_value:.1f}\np+q= {i_value:.1f}"

print(stmt+"\n")
print(stmt2.format(q_value=q, i_value=i,p_value=p))
