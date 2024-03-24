#37.print the person is eligible for donation of blood?(based on age and weight)
#Input: age=18 and weight=50 Output: eligible for donation of blood
#Input:age=18 and weight=48 Output:your weight is low so your not eligible for donation of blood.
#Input: age=17 and weigh=52 Output: your age is below to donate blood
a=int(input("enter you age"))
w=int(input("enter your weight"))
if a >= 18 and w >= 50:
        print("eligible for donation of blood")
elif a < 18:
        print("your age is below to donate blood")
else:
       print("your weight is low so you're not eligible for donation of blood")


