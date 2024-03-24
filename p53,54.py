#53.write a program to print 1 to n even numbers and odd numbers ?
a = int(input("Enter a number: "))

print("Even numbers:")
for i in range(2, a+1, 2):
    print(i)

print("Odd numbers:")
for i in range(1, a+1, 2):
    print(i)
