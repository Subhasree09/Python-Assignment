def power(a,b):
    if (b!=0):
        return a* power(a, b-1)
    else:
        return 1
    
a = int(input("Enter the number: "))
b = int(input("Enter the power: "))

p = power(a,b)
print(a," to the power of ",b,"is: ",p)