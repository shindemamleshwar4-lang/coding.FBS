start = int(input("enter starting number:"))
end = int(input("enter ending number:"))

print("armstrong number are:")

for num in range(start,end + 1):
    temp = num
    digit = len(str(num))
    total = 0
    while temp > 0:
        rem = temp % 10
        total = total + rem ** digit
        temp = temp // 10

        if total == num:
            print(num)