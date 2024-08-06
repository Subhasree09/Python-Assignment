def print_pattern(N):
    if N <= 0:
        return "N should be a positive integer"
    
    for i in range(1, N + 1):
        if i == 1:
            print(".")
        elif i < N  :
            print("/" + "\\")
        else:
            print("/" + "_" * (i - 1) + "\\")

N = int(input("Enter the number of levels (N): "))
print_pattern(N)
