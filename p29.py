#29. Write a program to print wishes based on time ?
#Input : < 12  
#Output : Good morning
#Input : > 12 and < 18
#Output : Good after noon
#Input : > 18 and < 24
#Output : Good night
t=int(input("enter a time"))
name=(input("enter Your name"))
if(t<=12):
    print("Good morning"+name)
elif(t>12& t<18):
    print(" Good after noon"+name)
elif(t>18& t<=24):
    print("Good night"+name)
elif(t<=25):    
     print("worng"+name)
else:
    print("worng"+name)