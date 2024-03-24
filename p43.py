#43.Write a program to print week days by using numbers (days should startfrom 0 index number)? Input: 1 Output: Monday Input: 7 above Output: invalid day
a=int(input("Enter a week number"))
if(a==0):
    print("Sunday")
elif(a==1):
    print("Monday")
elif(a==2):
    print("Tuesday") 
elif(a==3):
    print("Wedesday")
elif(a==4):
    print("Thursday")
elif(a==5):
    print("friday") 
elif(a==6):
    print("saturday")    
else:
    print("invalid days")               