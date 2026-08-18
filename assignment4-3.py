# WAP to print sum series upto n.

n = int(input("enter value = "))
sum = 0
for i in range(1,n+1):
    sum = sum + i # sum +=1
print("addition:",sum)