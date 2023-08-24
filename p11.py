#Write a program to check whether the given number is even or odd? Input: 2 Output: Given number is Even,Input :3 Output: Given number is odd
a=int(input("enter a first number"))
b=int(input("enter a second number"))
if a&b%2==0:
    print("its is even number")
elif b%2==0:
    print("its is even number")

else:
    print("its is a odd number")
