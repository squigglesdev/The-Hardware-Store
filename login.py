import dictCreator
import dictToJson
from getpass import getpass
import os
import json
def login():
    details = { "email":"", "phone":"", "username":"", "firstname":"", "surname":"", "password":""}
    begin = input("Do you have an account or would you like to create one?\nA: Create account\nB: Log in with existing account")
    if begin.upper() == "A":
        os.system("cls")
        contact = input("Ok. How do you want us to reach you?\nA: Email\nB: Phone")
        if contact.upper() == "A":
            os.system("cls")
            email = input("Great. What's your email address? We will only contact you if we detect any suspicious logins to your account.\nIf you would like to recieve promotions and updates, please enable that in your account preferences.\nEmail: ")
            confirm = input(f'Please confirm that your email address is "{email}". (Y/N)')
            if confirm.upper() == "Y":
                os.system("cls")
                print("Great! Remember you can always link multiple emails and a phone number in your account preferences.")
                details = dictCreator.saveDetails("email", email, details)
            else:
                pass # for until i have a proper failure iteration system going
        elif contact.upper() == "B":
            os.system("cls")
            phone = input("Great. What's your phone number? We will only contact you if we detect any suspicious logins to your account.\nIf you would like to recieve promotions and updates, please provide an email address and enable the promotion setting in your account preferences.\nPhone: ")
            confirm = input(f'Please confirm that your phone number is "{phone}". (Y/N)')
            if confirm.upper() == "Y":
                os.system("cls")
                print("Great! Remember you can always link an email account in your account preferences.")
                details = dictCreator.saveDetails("phone", phone, details)
            else:
                pass # for until i have a proper failure iteration system going
        else:
            pass # for until i have a proper failure iteration system going
        
        os.system("cls")
        name = input("Ok, now please tell us your full name.\nFull name: ")
        name = name.split()
        for i in name:
            if name.index(i) == 0:
                firstname = i
                details = dictCreator.saveDetails("firstname", firstname, details)
            else:
                surname = i
                details = dictCreator.saveDetails("surname", surname, details)
        os.system("cls")
        username = input("Perfect. Now please enter a username or alias you would like to sign in with.\nUsername: ")
        dictCreator.saveDetails("username", username, details)
        os.system("cls")
        password = getpass("It's now time to set a password. Please enter one: ")
        confirmedPassword = getpass("Please confirm your password by writing it again: ")
        if password == confirmedPassword:
            details = dictCreator.saveDetails("password", password, details)
        else:
            pass # for until i have a proper failure iteration system going
        account = dictToJson.toJson(details)
        os.system("cls")
        return username
    elif begin.upper() == "B":
        os.system("cls")
        f = open("userDetails/userDetails.json", "r")
        jsonData = f.readlines()
        user = input("Username: ")
        for i in jsonData:
            if user in i:
                record = json.loads(i)
                break
            else:
                continue
        
        if record != None:
            pwrd = input("Password: ")
            if record["password"] == pwrd:
                return user
            while record["password"] != pwrd:
                os.system("cls")
                pwrd = input("Password: ")
            
                
        else:
            print("Username invalid.")
