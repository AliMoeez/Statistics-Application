import matplotlib.pyplot as plt, numpy as np, pandas as pd
from sklearn import linear_model
from tkinter import *
from tkinter import filedialog

SCREEN=Tk()

SCREEN.geometry("1200x800") ; SCREEN.config(bg="gray0") ; SCREEN.title("Statistics Application") ; SCREEN.resizable(False,False)

file_label="" ; data="" ; data_label="" ; string="TEST"

class Home:
    def __init__(self,file_label,data,data_label,string):
        self.bg_colour="gray0" ; self.fg_colour="dodger blue"  ; self.file_label=Label(SCREEN,text="You have uploaded PASS",bg="gray0",fg="gray0") 
        self.file_label.configure(font=("Open Sans",10))  ; self.file_label.grid(column=1,row=3,ipady=20)
        self.title_label=Label(SCREEN,text="Statistics Application",bg=self.bg_colour,fg=self.fg_colour)  ; self.title_label.configure(font=("Open Sans",30))
        self.instrution_label=Label(SCREEN,text="Upload Your CSV/XLSX Files Below To Begin!",bg=self.bg_colour,fg=self.fg_colour) ; self.instrution_label.configure(font=("Open Sans",20))
        self.label_1=Label(SCREEN,text="",bg=self.bg_colour,fg=self.fg_colour) ; self.data=data ; self.data_label=data_label

    def file_upload(self):
        self.file=filedialog.askopenfilename(title="Upload CSV or XLSX Files",filetypes=(("CSV Files","*.csv"),("XLSX Files","*.xlxs")))
        self.file_label=Label(SCREEN,text=f"You have uploaded {self.file}",bg="gray0",fg="dodger blue") ; self.file_label.configure(font=("Open Sans",10)) ; self.file_label.grid(column=1,row=3,ipady=20)

    def text(self):
        self.title_label.grid(column=1,row=0,ipady=50) ; self.label_1.grid(column=0,row=0,ipadx=170) ; self.instrution_label.grid(column=1,row=1,ipady=20)
        
    def data_organization(self):
        self.upload_button=Button(SCREEN,text="Open File",command=lambda:Home.file_upload(self),bg=self.bg_colour,fg=self.fg_colour) ; self.upload_button.grid(column=1,row=2)
        self.file_text=self.file_label.cget("text")[18:]
        if self.file_text.endswith(".csv"): self.data=pd.read_csv(self.file_text)
        if self.file_text.endswith(".xlsx"): self.data=pd.read_excel(self.file_text)
        else : pass
        if self.file_text.endswith(".csv") or self.file_text.endswith(".xlsx"): self.data_label=Label(SCREEN,text=self.data.head(),bg=self.bg_colour,fg=self.fg_colour)
        else: self.data_label=Label(SCREEN,text=self.data,bg=self.bg_colour,fg=self.fg_colour)
        self.data_label.grid(column=1,row=6,pady=20)
        

    def confirmation_button(self):
        self.upload_button=Button(SCREEN,text="Confirm File",command=lambda:Home.data_organization(self),bg=self.bg_colour,fg=self.fg_colour) ; self.upload_button.grid(column=1,row=4,pady=20)
        self.file_text=self.file_label.cget("text")[18:]
        if (self.file_text.endswith(".csv") or self.file_text.endswith(".xlsx")) and self.string.get()=="Linear Regression":
           print("HERE")

    def data_clear(self):
        self.data_label.destroy() ; self.file_label.destroy()
    
    def data_clear_button(self):
        self.clear_button=Button(SCREEN,text="Clear File",command=lambda:Home.data_clear(self),bg=self.bg_colour,fg=self.fg_colour) ; self.clear_button.grid(column=1,row=5)

    def test_type(self):
        self.test_label=Label(SCREEN,text="Choose The Test You Want To Use",bg=self.bg_colour,fg=self.fg_colour) ; self.test_label.grid(column=1,row=8,pady=20)
        self.dropdown_test_options=["Linear Regression","Multiple Regression","T-Test","ARIMA"] ; self.string=StringVar() 
        self.test_dropdown=OptionMenu(SCREEN,self.string,*self.dropdown_test_options) ; self.test_dropdown.config(bg=self.bg_colour,fg=self.fg_colour) 
        self.test_dropdown["menu"].config(bg=self.bg_colour,fg=self.fg_colour) ; self.test_dropdown.grid(column=1,row=9)
        self.string.set(self.dropdown_test_options[0])

    def next_step(self):
        self.next_button=Button(SCREEN,text="Next",bg=self.bg_colour,fg=self.fg_colour,command=lambda:Home.confirmation_button(self)) ; self.next_button.grid(column=1,row=10,pady=20)

        

        
home=Home(file_label,data,data_label,string)
home.text()
home.data_organization()
home.test_type()
home.confirmation_button()
home.data_clear_button()
home.next_step()

SCREEN.mainloop()