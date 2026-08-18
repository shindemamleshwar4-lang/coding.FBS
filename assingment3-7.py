#WAP to check if user has entered correct user id and password.

userid = input("enter user id = ")
password = (input("enter password = "))

if userid == "admin" and password == "2004":
    print("login successful")
else:
    print("invalid user ID or password")
    