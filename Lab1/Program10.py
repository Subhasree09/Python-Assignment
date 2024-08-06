n = int(input("Enter the last limit: "))
a=0
b=1
for i in range(1, n+1):
    print(a)
    a, b = b , a+b