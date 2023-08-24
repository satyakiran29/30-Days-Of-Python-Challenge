#18. Write a program to check the given person's age is major or minor?
#Input: 18 Output: Given person age is major
#Input:17 Output: Given age is minor

a=int(input("enter your age"))
if a>=18:
    print("major")
elif a<=18:
    print("minor")
else:
    print("error")