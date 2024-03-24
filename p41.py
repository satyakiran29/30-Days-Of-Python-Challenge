#41.write a program to print as below format?
#Input: 1 Output: the number is 1
#Input:2 Output: the number is 2
#Input:3 Output: the number is 3
#Input:5 Output: the value is more than 3
n=int(input("enter a value:"))
 
match n:
   case 1:
    print("the number is 1")
   case 2:
    print("the number is 2")
   case 3:
    print("the number is 3") 
   case default:
    print("the value is more than 3")
       