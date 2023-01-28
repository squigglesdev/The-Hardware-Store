import secrets
import json

def saveDetails(type, data, details):
    if type == "email":
        details["email"] = data
    elif type == "phone":
        details["phone"] = data
    elif type == "username":
        details["username"] = data
    elif type == "firstname":
        details["firstname"] = data
    elif type == "surname":
        details["surname"] = data
    elif type == "password":
        details["password"] = data
    else:
        raise Exception("The acccount detail type is invalid.")
    return details
        
