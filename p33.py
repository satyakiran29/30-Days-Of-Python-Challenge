#33.print the given vowel is small letter (or) capital letter?
#Input: a
#Output: small letter
#Input: A
#Output:capital letter
#Input:b
#Output: consonant

c= input("Enter a character: ")
if c in ('a', 'e', 'i', 'o', 'u'):
    print(c, "is a Small letter")
elif c in ('A', 'E', 'I', 'O', 'U'):
    print(c, "is a Capital letter")
else:
    print(c, "is a Consonant")
