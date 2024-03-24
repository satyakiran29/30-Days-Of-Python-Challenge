#48.write a program to print the percentage and grade of a student.(of 5subjects)
#Input: 90,90,90,90,90 Output: 90 percentage and “A” grade
#Input:40,40,40,40,40 Output: 40 percentage and improve thee study

s1= int(input("enter a 1 subjet marks"))
s2= int(input("enter a 2 subjet marks"))
s3= int(input("enter a 3 subjet marks"))
s4= int(input("enter a 4 subjet marks"))
s5= int(input("enter a  5 subjet marks"))

t=s1+s2+s3+s4+s5
print(t)
p=t/500*100
print(p)

match p:
     case 90 :
        print(p)
        print("A Grade")
     case 80 ,70,:
        print(p)   
        print("B")
     case 60,50:
        print(p)   
        print("e")   
     case 40:
        print("fail")
        print("improve to study")   
