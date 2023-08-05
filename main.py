import matplotlib.pyplot as plt, numpy as np, pandas as pd
from sklearn import linear_model
from tkinter import *
from tkinter import filedialog

SCREEN=Tk()

SCREEN.geometry("1200x800") ; SCREEN.config(bg="gray0") ; SCREEN.title("Statistics Application") ; SCREEN.resizable(False,False)

class Home:
    def __init__(self):
        self.bg_colour="gray0" ; self.fg_colour="dodger blue"
        self.title_label=Label(SCREEN,text="Statistics Application",bg=self.bg_colour,fg=self.fg_colour)  ; self.title_label.configure(font=("Open Sans",30))
        self.instrution_label=Label(SCREEN,text="Upload Your CSV/XLSX Files Below To Begin!",bg=self.bg_colour,fg=self.fg_colour) ; self.instrution_label.configure(font=("Open Sans",20))
        self.label_1=Label(SCREEN,text="",bg=self.bg_colour,fg=self.fg_colour)

    def file_upload():
        file=filedialog.askopenfilename(title="Upload CSV or XLSX Files",filetypes=(("CSV Files","*.csv"),("XLSX Files","*.xlxs")))
        file_label=Label(SCREEN,text=f"You have uploaded {file}",bg="gray0",fg="dodger blue") ; file_label.configure(font=("Open Sans",10)) ; file_label.grid(column=1,row=3,ipady=20)

    def text(self):
        self.title_label.grid(column=1,row=0,ipady=50)
        self.label_1.grid(column=0,row=0,ipadx=170)
        self.instrution_label.grid(column=1,row=1,ipady=20)
        
    def button(self):
        self.upload_button=Button(SCREEN,text="Open File",command=Home.file_upload) ; self.upload_button.grid(column=1,row=2)
    
home=Home()
home.text()
home.button()

SCREEN.mainloop()