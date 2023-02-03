import loginwithgui
from tkinter import *
import cart
from item import *

username = None
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



#log in button
def logInEntry():
    global username
    username = loginwithgui.login("B", "A", "A", "A", "A", "A", "A", usernameInput.get(), passwordInput.get(), "A")
    print(username)
    if username != None:
        success.config(text="Success!")
        root.destroy()
        rootScreen()
    else:
        success.config(text="Try again.")
    
def signUpEntry():
    global username
    global logout
    global logOutImage
    username = loginwithgui.login("A", "A", emailInputSignUp.get(), "Y", "A", "A", nameInputSignUp.get(), usernameInputSignUp.get(), passwordInputSignUp.get(), passwordInputSignUp.get())
    if username != None:
        success.config(text="Success!")
        root.destroy()
        rootScreen()
    else:
        success.config(text="Try again.")

def logOut():
    global username
    username = None
    root.destroy()
    rootScreen()

def logIn():
    global logout
    global logOutImage
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

def rootScreen():
    global root

    try:
        logInScreen.destroy()
    except:
        pass
    #window
    root = Tk()
    root.geometry("850x450")
    root.resizable(False, False)
    root.title(" Hardware Store")
    root.config(bg="white")

    #top bar
    topbar = Label(root, bg="#9F649D")
    topbar.place(x=0, y=0, w=850, h=42)

    #logo
    logoImage = PhotoImage(file="HS.png")
    logo = Label(root, image= logoImage, bg="#9F649D")
    logo.place(x=17.5,y=9.17, w=27.5, h=24)


    searchImage = PhotoImage(file="unActiveSearch.png")
    searchBar = Button(root, image=searchImage, bg="#9F649D", relief=FLAT, bd=0, command=searchentry)
    searchBar.place(x=159.17, y=8.33, w=481.67, h=25)
    print(username)
    if username == None:
        loginImage = PhotoImage(file="login.png")
        login = Button(root, image=loginImage, bg="#9F649D", relief=FLAT, bd=0, command=logIn)
        login.place(x=707.5, y=8.33, w=75, h=25)
        Label(text="Please log in.", bg="white").place(x=31.25, y=123.75)
    else:
        logOutImage = PhotoImage(file="logout.png")
        logout = Button(root, image=logOutImage, bg="#9F649D", relief=FLAT, bd=0, command=logOut)
        logout.place(x=707.5, y=8.33, w=75, h=25)
        basketImage = PhotoImage(file= "basket.png")
        basket = Button(root, image=basketImage, bg="#9F649D", relief=FLAT, bd=0, command=cart.show)
        basket.place(x=787.5, y=8.33, w=25, h=25)
        hammer = Item(root, "Hammer", "A basic hammer. Nothing special.", "Builder's Equipment")
    
    

    root.mainloop()
rootScreen()

#user = login.login()
#print(f"Welcome to the Hardware Store, {user}!")

