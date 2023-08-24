#17. Write a program to check the given alphabet is Vowel or consonant?
#Input: a Output: A is Vowel
#Input : c Output: C is consonant
c= input("Enter a character: ")
if c in ('a', 'e', 'i', 'o', 'u'):
    print(c, "is a Vowel")
elif c in ('A', 'E', 'I', 'O', 'U'):
    print(c, "is a Vowel")
else:
    print(c, "is a Consonant")