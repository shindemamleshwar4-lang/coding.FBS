#write a program to reverse three-digit number.
n = int(input("Enter the three-digit number:"))

x = n // 100
y = (n //10) % 10
z = n % 10

reverse = (z * 100) + (y * 10) + x

print("reverse number = ", reverse)