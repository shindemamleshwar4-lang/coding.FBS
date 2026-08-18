#WAP to input all side of a triangle and check whether triangle is valid or not .

x = int(input("enter first number = "))
y = int(input("enter second number = "))
z = int(input("enter third number = "))

if (x + y > z) and (x + z > y) and (y + z > x):
    print("triangle is valid")
else:
    print("triangle is not valid")
    