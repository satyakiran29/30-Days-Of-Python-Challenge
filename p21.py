#21. write program to check whether a character is alphabet, digit or special character
#input : hello
#output : string
#input : 978
#output : Number
#input : @
#output : special character


c=(input("Enter a Charater"))

if(c >= 'a' and c <= 'z'):
    print("The Given Character ", c, "is an Alphabet")
elif (c >= 'A' and c <= 'Z'):    
    print("The Given Character ", c, "is an Alphabet")  
elif(c >= '0' and c <= '9'):
    print("The Given Character ", c, "is a Digit")
else:
    print("The Given Character ", c, "is Not an Alphabet or a Digit")