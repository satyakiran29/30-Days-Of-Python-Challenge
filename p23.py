#Program to print days in a month using logical OR operator
#input : 1
#output : 31 days like that;
mn= (input("Input the name of Month: "))

if mn == "2":
	print("No. of days: 28/29 days")
elif mn in ("4", "6", "9", "11"):
	print("No. of days: 30 days")
elif mn in ("1", "3", "5", "7", "8", "10", "12"):
	print("No. of days: 31 day")
else:
	print("Wrong month name") 