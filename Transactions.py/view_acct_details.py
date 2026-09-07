from write_read import read

def view_details(number):
    
    details = read()

    if number in details:
       name1 = details[number]["first_name"]
       name2 = details[number]["middle_name"]
       name3 = details[number]["last_name"]
       password = details[number]["password"]
       print(f"---- This are your acct details ----\n First_Name: {name1}\n Middle_Name: {name2}\n Last_Name: {name3}\n Password: {password}") 
    else:
        print("Unregistered Number!") 
            