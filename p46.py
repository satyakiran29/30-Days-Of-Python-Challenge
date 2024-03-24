#46.Write a program to print travel in the metro from where to where regarding
#ticket cost?
#Input: 15 Output: Miyapur to Jntu
#Input: 45 Output: Miyapur to Ameerpet
#Input: 65 Output: Please check ticket costs

b=int(input("ente a ticket cost"))



match b:
     case 65:
      print("Please check ticket costs")
     case 15:
       print("Miyapur to Jntu")
     case 45:
       print("Miyapur to Ameerpet")
     case deflaut:
        print(" Ticket not avilable")         