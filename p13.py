#13. Write a program to check whether the given number is positive or negative?
#Input: 2 Output: Given number is positive
#Input : -3 Output: Given number is negative
a= float(input("Enter a number: "))
if a > 0:
   print("Positive number")
elif a == 0:
   print("The number zero is neither positive nor negative")
else:
   print("Negative number")
