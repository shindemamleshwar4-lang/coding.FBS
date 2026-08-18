#WAP to print fibonacci series upto n.

n = int(input("how many fibonacci number you want ="))
a = -1
b = 1
for i in range(n):
    c = a + b
    print(c)

    a = b
    b = c