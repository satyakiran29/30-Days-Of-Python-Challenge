#16. Write a program using && in if condition, check the given number is divisible by 3 & 5.
#Input: 15 Output: 15 is divisible by 3 & 5
#Input: 18 Output: 18 15 is divisible by 3 & 5
a=int(input("enter a number"))
if (a%3==0) and (a%5==0):
    print( " Its is divisible by 3 & 5")
else:
    print("its is not divisible by 3 & 5")   