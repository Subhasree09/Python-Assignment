base = int(input("Enter the base number: "))
exp = int(input("Enter the exponent number: "))
p = 1
for i in range (1, exp+1):
    p = p * base

print (base," to the power of ",exp," is : ",p)