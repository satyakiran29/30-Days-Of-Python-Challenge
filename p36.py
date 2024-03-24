#.print the given number is even (Or) odd?
#Input: 5 Output: odd number
#Input:6 Output:even number
#Input: a Output: not a number

n=input("enter a number")


if (type(n) == int)  and (n % 2 == 0):
           print ("even number")
elif (type(n) == int)  and (n %  2!= 0):
            print ("odd number")
elif (type(n) == str):  
        print ("not a number")           
else:
        print ("not a number")


