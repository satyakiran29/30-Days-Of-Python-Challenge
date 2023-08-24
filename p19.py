#19. Write a program to check whether the given letter is in Uppercase/Lowercase?
#Input: A Output: A is in UppercaseInput: b Output : b is in lowercase.
c= input("Please Enter Your Own Character : ")

if(c >= 'A' and c <= 'Z'):
    print("The Given Character ", c, "is an Uppercase Alphabet") 
elif(c >= 'a' and c <= 'z'):
    print("The Given Character ", c, "is a Lowercase Alphabet")
else:
    print("The Given Character ", c, "is Not a Lower or Uppercase Alphabet")