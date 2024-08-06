num = int(input("Enter a number: "))
n = num
rev = 0
while num!=0 :
    last = num % 10
    rev = rev * 10 + last
    num = num // 10
print("The original number is: ",n)
print("The reversed number is: ",rev)
