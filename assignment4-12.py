# WAP to check if given number is armstrong number or not.
#(hint : 153 = 1*1*1 + 5*5*5 + 3*3*3, 1643 = 1*1*1*1 + 6*6*6*6 + 4*3*3*3 + 4*4*4*4)
 
num = int(input("enter a number:"))

temp = num
count = len(str(num))
sum = 0

while temp > 0:
    digit = temp % 10
    sum = sum + digit ** count
    temp = temp // 10

    if sum == num:
        print(num,"is an armstrong number")
    else:
        print(num, "is not an armstrong")