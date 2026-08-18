#a. 1! + 2! + 3! + ... + n!

n = int(input("Enter n: "))

fact = 1
sum = 0

for i in range(1, n + 1):
    fact = fact * i
    sum = sum + fact

print("Sum =", sum)


#b. N + N² + N³ + ... + Nᴺ

n = int(input("Enter N: "))

sum = 0

for i in range(1, n + 1):
    sum = sum + n ** i

print("Sum =", sum)

#c. Find the sum of a geometric series from 1 to n where the common ratio is 2.
n = int(input("Enter number of terms: "))

sum = 0
term = 1

for i in range(n):
    sum = sum + term
    term = term * 2

print("Sum =", sum)

#d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10

a = int(input("Enter a: "))

sum = 0

for i in range(1, 11):
    sum = sum + (a ** i) / i

print("S =", sum)

x = int(input("Enter x: "))
n = int(input("Enter number of terms: "))

sum = 0
sign = 1
denominator = 1


#e. x - x2/3 + x3/5 - x4/7 + .... to n terms
for i in range(1, n + 1):
    sum = sum + sign * (x ** i) / denominator
    sign = sign * -1
    denominator = denominator + 2

print("S =", sum)