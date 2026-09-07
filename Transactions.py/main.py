from create_acct import create_new
from login import user_login
from view_acct_details import view_details
from deposit import deposit

print("---- Welcome back -----\n 1.Login\n 2.Create Acct\n")

user_input = input("Select access: ")

while True:
   if user_input == "1":
        user_number = input("Enter Number or Email: ")  
        user_password = input("Enter Password: ")
        user_login(user_number, user_password)
        break  
           
   elif user_input == "2":
        first_name = input("Enter First name: ")
        middle_name = input("Enter Middle name: ")
        last_name = input("Enter Last Name: ")
        number = input("Enter Number or Email: ")
        login_password = input("Enter a Login Password: ")
        create_new(first_name, middle_name, last_name, number, login_password)
        print("---- Acct created successfully ----\n")
        break  
        
   else:
        print("Invalid selection. Please try again.")
        user_input = input("Select access: ")



print("---- Select Transaction ----\n 1.Deposit.\n 2.Transfer.\n 3.Withdraw.\n 4.View Balance.\n 5.Exit.")        

while True:
     user_input = input("Enter Transaction: ")
     if user_input == "1":
           user_number = input("Enter Number: ")
           user_amount = input("Enter Amount: ")
           deposit(user_number, user_amount)
           continue

     elif user_input == "":
               user_number = input("Enter Number: ") 
     view_details(user_number)
     continue
