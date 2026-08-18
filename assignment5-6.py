n = int(input("enter how many prime number you want:"))

count = 0
num = 2

print("fist",n,"prime number are:")

while count < n:
    for i in range(2,num):
        if num % i == 0:
            break
        else:
            print(num,end= " ")
            count +=1

            num += 1