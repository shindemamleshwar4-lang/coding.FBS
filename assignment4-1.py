#WAP print all even number untill n.

n = int(input("enter the value "))

for i in range(1, n + 1):
    if i % 2 == 0:
        print(i)
        