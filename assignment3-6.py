#WAP to calculate profit or loss.
cp = int(input("enter cost price ="))
sp = int(input("enter selling price ="))

if sp > cp:
    profit = sp - cp
    print("profit =", profit)
elif cp > sp:
    loss = cp - sp
    print("loss =",loss)
else:
    print("no profit no loss")