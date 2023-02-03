from tkinter import *

class Item:
    def __init__(self, root, name, description, category):
        self.name = name
        self.description = description
        self.category = category


        self.buttonImage = PhotoImage(file="Productbg.png")
        self.button = Button(root, image=self.buttonImage, bd=0, relief=FLAT)
        self.button.place(x=30.83, y=142.5, w=120, h=166.58)
    
    def __str__(self):
        return self.button