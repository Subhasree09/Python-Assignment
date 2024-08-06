d = int(input("Enter the decimal number: "))
s=0
d1=1
while(d!=0):
    r = d%2
    s = s+r*d1
    d = d//2
    d1 = d1 * 10

print("The Binary eqivalent of the number is: ",s)