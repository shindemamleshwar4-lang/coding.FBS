#WAP to check if a givan number is prime number or not.

num = int(input("enter a given number:"))

if num > 1:
    for i in range(2 , num):
        if num % i == 0:
            print(num,"is not a prime number")
            break
        else:
            print(num,"is not a prime number")
    else:
        print(num,"is not a prime number")
        