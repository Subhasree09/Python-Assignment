num = int(input("Enter a number: "))
n=num
rev=0
while(num!=0):
    last = num % 10
    rev = rev * 10 + last
    num = num // 10
if(rev == n):
    print("The number is a Palindrome Number")
else:
    print("The number is not a Palindrome Number") 