# WAP to prompt user to enter user id and password.
# after verifying userid and password,display a 4 digit random number and ask user to enter the same.
# if user enters the same number then show him success message otherwise failed.(something like captcha)

import random 
# correct user id and password 
userid = "admin"
password = "2004"

#input from user 
userid = input("enter user id =")
pwd = input ("enter password =")

#verify user id and password
if userid == "admin" and pwd == "2004":
    print("login successful")

    # generate a 4 digit random number
    captcha = random.randint(1000,9999)
    print("captcha:", captcha)

    # ask user to enter the same number
    user_input = int(input("Enter the captcha number:"))

    #verify the captcha 
    if user_input == captcha:
        print("login successful")
    else:
        print("captcha incorrect. login faild")

else:
    print("invalid user id or password. login password")