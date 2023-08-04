import matplotlib.pyplot as plt, numpy as np, pandas as pd
from sklearn import linear_model
from tkinter import *

SCREEN=Tk()

SCREEN.geometry("1200x800") ; SCREEN.config(bg="gray0") ; SCREEN.title("Statistics Application")

class Home:
    def __init__(self):
        self.title_label=Label(SCREEN,text="Statistics Application",bg="gray0",fg="dodger blue")
        self.title_label.configure(font=("Times New Roman",30))
    
    def text(self):
        self.title_label.pack()   


home=Home()
home.text()

SCREEN.mainloop()