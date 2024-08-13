import json
import menu as m
import new_contact 
import contacts
import key_order

tmp , data  , action = [] , [] , ''
data=contacts.get_list()
print(" * Welcome to the phone book *")

while(True):
    action = m.menu()   
    #Exit button
    if action=='7':
        break
    
    if action=='1':
        tmp=new_contact.get_info()
        data[len(data)+1]=tmp
        
    elif action=='2':
        flag , first , last = False,input("Which contact do you wish to change?\nFirst name: "),input("Last name: ")
        #finding the contact
        for key in data:
            if data[key][0]==first:
                if data[key][1]==last:
                    print("Enter the new information:\n")
                    data[key]=new_contact.get_info()
                    flag=True
                    break
        if flag==False:
            print("\nContact not found !")       
                    
    elif action=='3':
        flag , first , last = False,input("Which contact do you wish to remove?\nFirst name: "),input("Last name: ")
        for key in data:
            if data[key][0]==first:
                if data[key][1]==last:
                    del(data[key])
                    flag=True
                    break
        if flag==False:
            print("\nContact not found !")
            
        #after removing, keys need to be reorganized :
        data=key_order.fix_it(data)
        
    elif action=='4':
        print("\nHere is your current contact list:")
        if len(data)==0:
            print("[]")
        else:
            for i in data:
                print(f"contact number {i}: {data[i]}")
        
    
    elif action=='5':
        data = dict(sorted(data.items(),key=lambda item: item[1][0]))        
        print("Sorting by name was successful!")
        
        #after sorting, keys need to be reorganized :
        data=key_order.fix_it(data)
        
    elif action=='6':
        #save            
        with open("phonebook.json","w") as f :
            json.dump(data,f)
        
    else:
        print("Not a valid option ! Try again.")

print("Goodbye!")

        

                
                
    
    
