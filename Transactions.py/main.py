from create_acct import create_new
from login import user_login
from view_acct_details import view_details
from deposit import deposit
from transfer import transfer
from withdraw import withdraw
from view_balance import view_balance
from history import users_history
from exit import exit

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

        try:
           pin =  int(input("Enter pin: "))
        except ValueError:
             print("Pin can only be numbers")
        create_new(first_name, middle_name, last_name, number, login_password, pin)
        print("---- Acct created successfully ----\n")
        break  
        
   else:
        print("Invalid selection. Please try again.")
        
   


print("---- Select Transaction ----\n 1.Deposit.\n 2.Transfer.\n 3.Withdraw.\n 4.View Balance.\n 5.View Acct Details.\n 6.History\n 7.Exit.")        

while True:
     user_input = input("Enter Transaction: ")
     if user_input == "1":
           user_number = input("Enter Number: ")
           try:
              user_amount = float(input("Enter Amount: "))
           except ValueError:
                print("Amount can only be digits")   
           deposit(user_number, user_amount)
           continue

     elif user_input == "2":
          user_number = input("Enter Your Number: ")
          acct_number = input("Enter acct_Number: ")
          try:
               amount = float(input("Enter amount: "))
          except ValueError:
               print("Invalid Syntax!")  
          user_password = input("Enter Password: ")
          transfer(user_number, acct_number, amount, user_password)
          continue  

     elif user_input == "3":
          user_number = input("Enter number: ")
          user_password = input("Enter Password: ")
          try:
             amount = float(input("Enter Amount: "))
          except ValueError:
               print("Invalid Syntax!")
          withdraw(user_number, user_password, amount)
          continue  

     elif user_input == "4":
          user_number = input("Enter number: ") 
          user_password = input("Enter Password: ")
          view_balance(user_number, user_password)
          continue

     elif user_input == "5":
          user_number = input("Enter Number: ")
          view_details(user_number)
          continue
     elif user_input == "6":
          user_number = input("Enter Number: ")
          users_history(user_number)

     elif user_input == "7":
          exit()
          break
     else:
          print("Invalid Input")