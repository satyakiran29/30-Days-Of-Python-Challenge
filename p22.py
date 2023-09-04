#22. write a program to check the maximum number among 3 numbers
#input : a=20;b=30,c=35
#output : c is maximum value
#input: a = 10; b= 43; c=34
#output : b is maximum value
#input : a= 45;b =33; c = 21;
#output : a is maximum value

n1 = float(input("Enter first number:"))
n2 = float(input("Enter second number:"))
n3 = float(input("Enter third number:"))

if (n1 >= n2) and (n1 >= n3):
   largest = n1
elif (n2 >= n1) and (n2 >= n3):
   largest = n2
else:
   largest = n3


print("The largest number is", largest)