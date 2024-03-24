#31. Write a program to take user name and password and print username and
#password are correct or not

username = "satya"
password = "123"
input_username = input("Enter username: ")
input_password = input("Enter password: ")

if input_username != username:
    print("Username is incorrect, try again")
elif input_password != password:
    print("password is incorrect, try again")
else:
     print("Login successfully")
