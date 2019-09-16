# 28. While Loop In Python
"""
# With the break statement we can stop the loop even if the while condition is true.
# With the continue statement we can stop the current iteration and continue with the next.
"""
i =0
while i <= 10:
    i+=1
    if i==3:
        continue
    else:
        if i == 6:
            break
        print(i)
