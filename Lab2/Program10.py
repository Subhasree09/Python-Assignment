num = int(input("Enter a number: "))
n = num
sum = 0
while(n!=0):
    l = n%10
    fact =1
    for i in range (1, l+1):
        fact = fact * i
    sum = sum + fact
    n = n//10

if(sum == num ):
    print("The number is a Krishnamurthy number ")
else:
    print("The number is not a Krishnamurthy number ")
