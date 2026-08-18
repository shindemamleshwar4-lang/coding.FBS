#A. children below 12 = 30% discount
#B. senior citizen (above 59) = 50% discount
#c. other need to pay full.

passanger = int(input("Enter the number of passenger:"))
cost = int(input("Enter the cost of ticket:"))

for i in range(passanger):
    print("passenger no" ,i+1)
    final_cost = 0
    age = int(input("Enter the age of passenger:"))
    if age<12:
        final_cost = cost-(cost*30)/100
        print(f"the final cost to travle for you is:{final_cost}")
    elif age>59:
        final_cost = cost - (cost*30)/100
        print(f"the final cost to travel for you is:{final_cost}")
    else:
        print(f"the final cost to traval for you is:{cost}")