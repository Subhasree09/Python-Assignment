def Calculate_slope(x1, x2, y1, y2):
    if x2 == x1 :
        return "Undefined"
    else:
        slope  = (y2-y1)/(x2-x1)
        return slope
    
x1 = int(input("Enter the value of x1: "))
x2 = int(input("Enter the value of x2: "))
y1 = int(input("Enter the value of y1: "))
y2 = int(input("Enter the value of y2: "))
s=Calculate_slope(x1,x2,y1,y2)
print("The slope is: ",s)
    
