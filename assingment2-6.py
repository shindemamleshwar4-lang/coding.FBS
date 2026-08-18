#WAP to calculate total salary of employee based on basic,da=10% of basic,
#ta=12% of basic, hra=15% of basic.

basic = int(input("basic salary of employee is :-"))

da_amt =(basic * 10) / 100
ta_amt =(basic *12) / 100
hra_amt =(basic * 15) / 100

total_salary = basic + da_amt + hra_amt
print("total salary of employee is :-",total_salary)