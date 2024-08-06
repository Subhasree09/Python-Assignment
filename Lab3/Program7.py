import math
def compute_sin(x,n):
    sine = 0
    for i in range(n):
        sign = (-1) ** i
        term = (x ** (2*i+1)) / math.factorial(2*i+1)
        sine = sine + (sign * term)
    return sine

x = float(input("Enter the value of x: "))
n = int(input("Enter the number of terms: "))

sin = compute_sin(x,n)
print(f"The Computed value of sin({x}) using {n} terms is: {sin}")