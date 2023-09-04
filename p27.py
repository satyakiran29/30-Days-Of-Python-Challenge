#27. Print the metro stations based on ticket cost?
#Input: Rs 10 Output: miyapur to jntu
#Input: Rs 20 Output: miyapur to kukatpally
#Input: Rs 30 Output: miyapur to bharat nagar
#Input: Rs 65 Output: ticket cost is up to Rs 60 .


a= (input("Input ticket costr: "))

if a ==10:
	print(" miyapur to jntu")
elif a ==20:
	print("miyapur to kukatpally")
elif a ==30:
	print("miyapur to bharat nagar")
elif a ==65:
	print("ticket cost is up to Rs 60")        
else:
	print("Error") 