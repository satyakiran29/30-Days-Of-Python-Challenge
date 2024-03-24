#32.Print the biggest number among 4 numbers?
#Input : a=10;b=25;c=30;d=5; Output: “C” is the big number.

n1 = float(input("Enter first number:"))
n2 = float(input("Enter second number:"))
n3 = float(input("Enter third number:"))
n4 = float(input("Enter  forth number"))
if (n1 >= n2) and (n1 >= n3) and (n1 >= n4):
   print("The largest number A is",n1)
   if (n2 >= n1) and (n2 >= n3) and  (n2 >= n4):
      print("The largest number B is",n2)
if (n3 >= n1) and (n3 >= n2) and (n3 >= n4):
        print("The largest number C is",n3)
elif (n4 >= n1) and (n4 >= n2)  and (n4 >= n3):
     print("The largest number D is",n4)     
else:
     print("error")


