org_id = "rajjj@8767"
org_pass = "1234"

for i in range (3):

    id = input("Enter user id:")
    password = input("Enter password")
    if id == org_id and password==org_pass:
        print("welcome user:")
    else:
        print("wrong credentials try again:-")
else:
    print("you are out of atempt")