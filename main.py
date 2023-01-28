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

def logIn():
    # TODO make this have the same visual stlye as the rest of the app
    global usernameInput
    global passwordInput
    global success
    global logInScreen
    logInScreen = Tk()
    logInScreen.geometry("850x450")
    logInScreen.resizable(False, False)
    logInScreen.title(" Hardware Store | Log in")
    usernameInput = Entry(logInScreen)
    usernameInput.pack(pady=20)
    passwordInput = Entry(logInScreen)
    passwordInput.pack(pady=20)
    enter = Button(logInScreen, text="Log In", command=logInEntry)
    enter.pack(pady=20)
    success = Label(logInScreen, text="")
    success.pack(pady=20)

    logInScreen.mainloop()


loginImage = PhotoImage(file="login.png")
login = Button(root, image=loginImage, bg="#9F649D", relief=FLAT, bd=0, command=logIn)
login.place(x=707.5, y=8.33, w=75, h=25)




root.mainloop()

#user = login.login()
#print(f"Welcome to the Hardware Store, {user}!")

