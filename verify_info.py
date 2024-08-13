import re

def validate_email(email: str) -> bool:
    flag = False
    
    if(re.match(r'^[a-zA-Z1-9\.\_]+@[a-zA-Z1-9]+\.[a-zA-Z]{3}$',email)):
        flag=True
    
    return flag


def validate_phone(number: str) -> bool:
    flag = False
    
    if(re.match(r'^09[0-9]{9}$',number)):
        flag=True
    elif(re.match(r'^\+989[0-9]{11}$',number)):
        flag=True
    elif(re.match(r'^00989[0-9]{12}$',number)):
        flag=True
    
    return flag
