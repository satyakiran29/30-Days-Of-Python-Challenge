#57. write a program to print 1 to n prime numbers ?
#input : n = 10;
#output : 2,3,5,7

a=int(input("enter a value"))
for i  in range (1,a):
     if(i%2!=0):
       print("Prime Number")
       print(i)
