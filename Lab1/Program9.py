num = int(input("Enter the number: "))
sum = 0
for i in range (1, num):
    if(num % i ==0):
        sum = sum + i

if(sum == num):
    print("The number is a perfect number")
else:
    print("The number is not a perfect number")

n= num
m = n
c=0
s=0
while(num!=0):
    num = num// 10
    c = c+1

while(m!=0):
    last = m % 10
    s = s+(last**c)
    m = m// 10

if(n == s):
    print("The number is an armstrong number")
else:
    print("The number is not an armstrong number")