#35. Print the boy and girl is eligible for marriage?
#Input: boy=18; girl=18 Output: both are eligible for marriage
#Input: boy=18; girl=17 Output: boy is eligible for marriage
#Input: boy=17;girl=18 Output: girl is eligible for marriage.
#Input: boy=17;girl=17 Output:boy and girl is not eligible for marriage
boy=int(input("enter boy age"))
girl=int(input("enter boy age"))
if boy>= 18 and girl >= 18:
       print("both are eligible for marriage")
elif boy >= 18:
        print("boy is eligible for marriage")
elif girl >= 18:
      print(" girl is eligible for marriage")
else:
       print("boy and girl is not eligible for marriage")


