#Beginner level login system easy 

username="avinash"                              #vaues of username and password
password="4518"
 
correct_username=input("enter username: ")      #taking input for login
correct_password=input("enter password : ")

if username==correct_username and password==correct_password :
    print("Welcome you loged in successfully")
    
else :
    print("Invalid username or password")