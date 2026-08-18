# write a program to check if person is eligibal to marry or not (male age >=21 and female age>=18)
# input gender and age 
gender = input("enter gender(male/female):")
age = int(input("enter age:"))

# check aligibality
if (gender == "male" and age >=21) or (gender == "female" and age >=18):
    print("eligible for marrige")
else:
    print("not eligibal for marrige")