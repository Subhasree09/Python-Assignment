n=int(input("Enter the limit: "))
p=1


for i in range(1,n+1):
    print(i," 1",end=" ")
    p=1
    for j in range(1,4):
        p = p * i
        print(p,end=" ")
    print()

