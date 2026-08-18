# 4. WAP to print factorial of a number.


n = int(input("enter value = "))
fact = 1
for i in range(1, n+1):
    fact = fact * i
print("factorial is =", fact)
