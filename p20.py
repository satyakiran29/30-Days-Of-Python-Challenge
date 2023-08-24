#20. Write a program to calculate profit or loss?
#Input: Cost of product : 1000, Spelling Price: 1500
#Output: Profit is 500
cp=int(input("enter a Cost of product:"))
sp=int(input("enter a   Spelling Price"))

if(cp > sp):
    ta= cp - sp
    print("Total Loss Amount = {0}".format(ta))
elif(sp > cp):
    ta = sp - cp
    print("Total Profit = {0}".format(ta))
else:
    print("No Profit No Loss!!!")