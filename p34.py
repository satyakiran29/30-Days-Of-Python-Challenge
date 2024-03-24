#34.print the person is eligible for government job (Or) not?(based on age)
#Input: age=17
#Output: your age is below to work
#Input:age=25 : your eligible for work
#Input:age=60 Output Your eligible to take pension.
age=int(input("Enter your age"))

if (age==0):
    print("your age is below to work")
elif (age>=25):
        print("your eligible for work")
elif(age>=60):
    print("Your eligible to take pension.")
else:
    print("error")    