num = int(input("Enter a number: "))
sum = 0
while(num !=0):
    l = num % 10
    sum = sum + l
    num = num // 10

print("The sum of the digits is: ",sum)
