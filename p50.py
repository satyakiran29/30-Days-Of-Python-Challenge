#50. write a program to print the cost a laptop?
#Input: hp Output:35k
#Input: dell Output:40k
a =input("Enter a company")
match a:
     case "hp" :
      print("35k")
     case "dell": 
        print("40k")
     case "acer":
        print("28k")
     case deflaut:
        print("Enter dell, hp or dell")    