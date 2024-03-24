#58. write a program to print n prime numbers ?
#input : n = 10;
#output : 2,3,5,7,11,13,17,19,23,29
a=int(input("enter a value"))
for i  in range (1,a):
     if(i%2!=0):
       print(i)
