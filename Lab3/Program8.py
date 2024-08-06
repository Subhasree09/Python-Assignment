import math
def compute_cos(x,n):
    cosine = 0
    for i in range(n):
        sign = (-1) ** i
        term = (x ** (2*i)) / math.factorial(2*i)
        cosine = cosine + (sign * term)
    return cosine

x = float(input("Enter the value of x: "))
n = int(input("Enter the number of terms: "))

cos = compute_cos(x,n)
print(f"The Computed value of cos({x}) using {n} terms is: {cos}")