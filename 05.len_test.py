# 05. len()


x, y, z = "apple ", "orange", " limon"
print("x= "+ x + "\ny= " + y + "\nz= " + z)

basket = x + y + z
print("\nmain value of basket= " + basket)

print("Using len() Function")
print(len(basket))
print(basket[:5])
print(basket[6:12])
print(basket[13:])

print("\n")
print("Using append() Function")
arr = []
arr.append(basket[:5])
arr.append(basket[6:12])
arr.append(basket[13:])
print(arr)

print("\n")
print("Using len() Function & for Loop")
n = 6
c = [basket[i:i+n] for i in range(0, len(basket), n)]
print(c)
