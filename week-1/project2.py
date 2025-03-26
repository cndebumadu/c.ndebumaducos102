R = int(input("what is your rate?: "))
T = int(input("what is your time?: "))
P = int(input("what is your principle?: "))
n = int(input("how many years?: "))
M = int(input("type it in: "))
A = P * M * T * (((1 + (R / n) ** (n * T) - 1) / (R / n)))
print("your compound interest interest is: ", A)

















