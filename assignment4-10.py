#10.WAP to check if givan number is perfect number.

num = int(input("enter a number:"))

sum = 0

for i in range (1,num):
    if num % i == 0:
        sum = sum + 1

if sum == num:
    print(num,"is a perfect number")
else:
    print(num,"is not a perfect number")