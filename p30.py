#30. Program to check equilateral, scalene or isosceles triangle
#input : side 1 : 60 side 2 : 60 side 3 : 60
#output : equilateral triangle
#input : side 1 : 90 side 2 : 45 side 3 : 45
#output : isosceles triangle
#input : side 1 : 40 side 2 : 50 side 3 : 90
#output : scalene triangl
a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))


if a == b and b == c:
        print ("Equilateral triangle")
elif a == b or b == c or a == c:
        print ("Isosceles triangle")
else:
        print ("Scalene triangle")




