import json
import re 
import verify_info as vf

def get_info():  
    temp_con=[]
    temp_con.append(input("First name: "))
    while (re.match(r'^[a-zA-Z]{1,40}$',temp_con[0]))==None:
        temp_con[0] = input("Incorrect first name! Please re-enter: ")
        
    temp_con.append(input("Last name: "))
    while re.match(r'^[a-zA-Z]{1,40}$',temp_con[1])==None:
        temp_con[1]=input("Incorrect last name! Please re-enter: ")

    temp_con.append(input("Phone number: "))
    while vf.validate_phone(temp_con[2])==False:
        temp_con[2]=input("Incorrect phone number! Please re-enter: ")
    
    temp_con.append(input("Email: "))
    while vf.validate_email(temp_con[3])==False:
        temp_con[3]=input("Incorrect email address! Please re-enter: ")
        
    return temp_con