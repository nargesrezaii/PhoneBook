import json
def get_list():
    with open("phonebook.json","r") as f:
        data = json.load(f)
    return data
