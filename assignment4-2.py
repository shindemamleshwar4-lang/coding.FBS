# 2. WAP to print all odd number until n.

n = int(input("enter the value of n:"))

print("odd number up to",n,"are:")

for i in range (1, n+1, 2):
    print(i)