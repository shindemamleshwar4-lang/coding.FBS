#WAP  to input angles of a triangle and check whether triangle is valid or not.

x = int(input("Enter first number ="))
y = int(input("Enter second number ="))
z = int(input("Enter third number = "))

if x + y + z ==180:
    print("triangle is valid")
else:
    print("triangle is nor valid")
    