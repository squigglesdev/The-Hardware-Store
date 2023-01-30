import loginwithgui
from tkinter import *

#window
root = Tk()
root.geometry("850x450")
root.resizable(False, False)
root.title(" Hardware Store")

#top bar
topbar = Label(root, bg="#9F649D")
topbar.place(x=0, y=0, w=850, h=42)

#logo
logoImage = PhotoImage(file="HS.png")
logo = Label(root, image= logoImage, bg="#9F649D")
logo.place(x=17.5,y=9.17, w=27.5, h=24)

#search bar
# TODO fix this custom search bar
def check(event):
    print(root.focus_get(), event.widget)
    if event.widget != search:
        print("done")
        search.pack_forget()
        #search = None

def searchentry():
    global search
    search = Entry(root, bd=0, font="Inter", bg="white")
    search.place(x=163, y=15, w=475, h=12)
    search.bind('<FocusOut>', check)
searchImage = PhotoImage(file="unActiveSearch.png")
searchBar = Button(root, image=searchImage, bg="#9F649D", relief=FLAT, bd=0, command=searchentry)
searchBar.place(x=159.17, y=8.33, w=481.67, h=25)


#log in button
def logInEntry():
    global username
    username = loginwithgui.login("B", "A", "A", "A", "A", "A", "A", usernameInput.get(), passwordInput.get(), "A")
    if username != None:
        success.config(text="Success!")
        logInScreen.after(360, logInScreen.destroy)
    else:
        success.config(text="Try again.")
def signUpEntry():
    global username
    username = loginwithgui.login("A", "A", emailInputSignUp.get(), "A", "A", "A", nameInputSignUp.get(), usernameInputSignUp.get(), passwordInputSignUp.get(), "A")
    if username != None:
        success.config(text="Success!")
        logInScreen.after(360, logInScreen.destroy)
    else:
        success.config(text="Try again.")

def logIn():
    # TODO make this have the same visual stlye as the rest of the app
    global usernameInput
    global passwordInput
    global usernameInputSignUp
    global passwordInputSignUp
    global emailInputSignUp
    global nameInputSignUp
    global success
    global logInScreen
    logInScreen = Tk()
    logInScreen.geometry("850x450")
    logInScreen.resizable(False, False)
    logInScreen.title(" Hardware Store | Log in")
    titlelogIn = Label(logInScreen, text="Log in")
    titlelogIn.grid(row=0, column=0, sticky=W, pady=2, padx=5)
    usernameLabel = Label(logInScreen, text="Username:")            #Username:
    usernameLabel.grid(row=1, column=0, sticky=W, pady=2, padx=5)
    usernameInput = Entry(logInScreen)                              #userentry
    usernameInput.grid(row=1, column=1, sticky=W, pady=2, padx=5)
    passwordLabel = Label(logInScreen, text="Password:")            #Password:
    passwordLabel.grid(row=2, column=0, sticky=W, pady=2, padx=5)
    passwordInput = Entry(logInScreen)                              #pwrdentry
    passwordInput.grid(row=2, column=1, sticky=W, pady=2, padx=5)
    enter = Button(logInScreen, text="Log In", command=logInEntry)  #[Enter]
    enter.grid(row=3, column=0, sticky=W, pady=2, padx=5)
    success = Label(logInScreen, text="")                           #Success!
    success.grid(row=4, column=0, sticky=W, pady=2, padx=5)



    # TODO add sign up options
    titleSignUp = Label(logInScreen, text="Sign up")
    titleSignUp.grid(row=0, column=4, sticky=W, pady=2, padx=5)
    usernameLabelSignUp = Label(logInScreen, text="Username:")
    usernameLabelSignUp.grid(row=1, column=4, sticky=W, pady=2, padx=5)
    usernameInputSignUp = Entry(logInScreen)
    usernameInputSignUp.grid(row=1, column=5, sticky=W, pady=2, padx=5)
    passwordLabelSignUp = Label(logInScreen, text="Password:")
    passwordLabelSignUp.grid(row=2, column=4, sticky=W, pady=2, padx=5)
    passwordInputSignUp = Entry(logInScreen)
    passwordInputSignUp.grid(row=2, column=5, sticky=W, pady=2, padx=5)
    emailLabelSignUp = Label(logInScreen, text="Email:")
    emailLabelSignUp.grid(row=3, column=4, sticky=W, pady=2, padx=5)
    emailInputSignUp = Entry(logInScreen)
    emailInputSignUp.grid(row=3, column=5, sticky=W, pady=2, padx=5)
    nameLabelSignUp = Label(logInScreen, text="Full Name:")
    nameLabelSignUp.grid(row=4, column=4, sticky=W, pady=2, padx=5)
    nameInputSignUp = Entry(logInScreen)
    nameInputSignUp.grid(row=4, column=5, sticky=W, pady=2, padx=5)
    signUpBttn = Button(logInScreen, text="Sign Up", command=signUpEntry)
    signUpBttn.grid(row=5, column=4, sticky=W, pady=2, padx=5)
    logInScreen.mainloop()


loginImage = PhotoImage(file="login.png")
login = Button(root, image=loginImage, bg="#9F649D", relief=FLAT, bd=0, command=logIn)
login.place(x=707.5, y=8.33, w=75, h=25)

root.mainloop()

#user = login.login()
#print(f"Welcome to the Hardware Store, {user}!")

