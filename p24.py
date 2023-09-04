#24 .Write a program to input marks of five subjects Physics, Chemistry,
#Biology, Mathematics and Computer. Calculate percentage and grade
#according to following:
#Percentage >= 90% : Grade A
#Percentage >= 80% : Grade B
#Percentage >= 70% : Grade C
#Percentage >= 60% : Grade D
#Percentage >= 40% : Grade E
#Percentage < 40% : Grade 

a=int(input("Enter marks of the first subject: "))
b=int(input("Enter marks of the second subject: "))
c=int(input("Enter marks of the third subject: "))
d=int(input("Enter marks of the fourth subject: "))
e=int(input("Enter marks of the fifth subject: "))
t=a+b+c+d+e
print(t)
p=t/500*100
print(p)
if (p>=90):
    print("Grade: A")
elif (p>=80) and (p<90):
    print("Grade: B")
elif (p>=70) and (p<80): 
    print("Grade: C")
elif (p>=60) and (p<70):
    print("Grade: D")
elif (p>=50) and (p<60):
    print("Grade: E")    
else:
    print("Grade: F")

    