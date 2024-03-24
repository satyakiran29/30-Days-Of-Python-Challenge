#45. Write a program to print operation between two numbers regarding
#operands?(simple calculator)
#input : 2/2 output : 1
a=int(input("ente a 1 value"))
b=int(input("ente a 2 value"))

x=(input("enter a operator"))

match x:
     case "+":
      c=a+b
      print(c)
    
     case "-":
       c=a-b
       print(c)
     case "*":
       c=a*b
       print(c)
     case "/":
       c=a/b
       print(c)
     case deflaut:
        print(" Enter  a Operators")         