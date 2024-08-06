n = int(input("Enter a number: "))
m = int(input("Enter another number: "))
p = n*m
gcd = 0
for i in range (1, p+1):
    if(n%i==0 and m%i==0):
        gcd = i
print("GCD is: ",gcd)