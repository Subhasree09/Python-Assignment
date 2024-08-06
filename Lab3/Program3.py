import cmath
def solve_quadratic_eqn(a,b,c):
    discriminant = b**2 - 4*a*c

    if discriminant > 0 :
        root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
        root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
        return (root1.real, root2.real)
    elif discriminant == 0 :
        root = -b / (2 * a)
        return root
    else:
        root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
        root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
        return (root1, root2)
    
a=float(input("Enter 1 number :"))
b=float(input("Enter 2 number :"))
c=float(input("Enter 3 number :"))

s1, s2 = solve_quadratic_eqn(a,b,c)

print(f"The solutions are {s1} and {s2}")