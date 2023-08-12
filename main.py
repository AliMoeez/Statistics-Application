import matplotlib.pyplot as plt, numpy as np, pandas as pd
from sklearn import linear_model
from tkinter import *
from tkinter import filedialog

SCREEN=Tk()

SCREEN.geometry("1200x800") ; SCREEN.config(bg="gray0") ; SCREEN.title("Statistics Application") ; SCREEN.resizable(False,False)

file_label="" ; data="" ; data_label="" ; string="TEST" ; dropdown_test_options_logic=[(0,0),(0,0),(0,0),(0,0)]

line_reg_model=False
mult_reg_model=False
ttest_model=False
ARIMA_model=False

class Home:
    def __init__(self,file_label,data,data_label,string,dropdown_test_options_logic):
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
        global line_reg_model, mult_reg_model,ttest_model,ARIMA_model
        self.upload_button=Button(SCREEN,text="Confirm File",command=lambda:Home.data_organization(self),bg=self.bg_colour,fg=self.fg_colour) ; self.upload_button.grid(column=1,row=4,pady=20)
        self.file_text=self.file_label.cget("text")[18:]
        self.dropdown_test_options_logic=[["Linear Regression",line_reg_model],["Multiple Regression",mult_reg_model],["T-Test",ttest_model],["ARIMA",ARIMA_model]]
        for idx,analysis_type in enumerate(self.dropdown_test_options_logic):
            if (self.file_text.endswith(".csv") or self.file_text.endswith(".xlsx")) and self.string.get()==self.dropdown_test_options_logic[idx][0]:
                self.dropdown_test_options_logic[idx][1]=True

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
        self.next_button=Button(SCREEN,text="Next",bg=self.bg_colour,fg=self.fg_colour,command=lambda:[Home.confirmation_button(self),LinearRegression.next_step_window(self)]) 
        self.next_button.grid(column=1,row=10,pady=20)

class LinearRegression(Home):
    def __init__(self):
        super().__init__(file_label,data,data_label,string,dropdown_test_options_logic) 
        self.dropdown_test_options_logic=dropdown_test_options_logic

    def next_step_window(self):
        if self.dropdown_test_options_logic[0][1]:
            self.SCREEN_POPUP=Tk() ; self.SCREEN_POPUP.geometry("600x250") ; self.SCREEN_POPUP.config(bg=self.bg_colour) ; self.SCREEN_POPUP.title("Linear Regression Settings") ; self.SCREEN_POPUP.resizable(False,False)
            LinearRegression.next_step_window_entries(self)
            LinearRegression.next_step_window_labels(self)
            LinearRegression.run(self)

    def next_step_window_entries(self):
        if self.dropdown_test_options_logic[0][1]:
            self.y_variables_entry=Entry(self.SCREEN_POPUP) ; self.y_variables_entry.grid(column=1,row=3) ; self.y_variables_entry.config(bg=self.bg_colour, fg=self.fg_colour)
            self.x_variables_entry=Entry(self.SCREEN_POPUP) ; self.x_variables_entry.grid(column=1,row=5) ; self.x_variables_entry.config(bg=self.bg_colour, fg=self.fg_colour)
            self.alpha_level_entry=Entry(self.SCREEN_POPUP) ; self.alpha_level_entry.grid(column=1,row=7) ; self.alpha_level_entry.config(bg=self.bg_colour, fg=self.fg_colour)
    
    def get_entry_values(self):
        if self.dropdown_test_options_logic[0][1]:
            for col in self.data:
                try:
                    if col in [self.y_variables_entry.get(),self.x_variables_entry.get()] and float(self.alpha_level_entry.get()):
                        self.error_input_text.destroy()
                    else:
                        self.error_input_text=Label(self.SCREEN_POPUP,text="ERROR: Check Your Input Boxes For Invalid Inputs.",fg=self.fg_colour,bg=self.bg_colour) ; self.error_input_text.grid(column=1,row=9) ; self.error_input_text.configure(font=("Open Sans",10)) 
                except Exception:
                    self.error_input_text=Label(self.SCREEN_POPUP,text="ERROR: Check Your Input Boxes For Invalid Inputs.",fg=self.fg_colour,bg=self.bg_colour) ; self.error_input_text.grid(column=1,row=9) ; self.error_input_text.configure(font=("Open Sans",10)) 

    def next_step_window_labels(self):
        if self.dropdown_test_options_logic[0][1]:
            self.placeholder_text=Label(self.SCREEN_POPUP,text="",fg=self.fg_colour,bg=self.bg_colour) ; self.placeholder_text.grid(column=0,row=0,padx=70)
            self.linereg_text=Label(self.SCREEN_POPUP,text="Enter Your Parameters Below",fg=self.fg_colour,bg=self.bg_colour) ; self.linereg_text.grid(column=1,row=0) ; self.linereg_text.configure(font=("Open Sans",18)) 
            self.y_variables_label=Label(self.SCREEN_POPUP,text="Dependent Variable (Y)",bg=self.bg_colour,fg=self.fg_colour) ; self.y_variables_label.grid(column=1,row=2) ; self.y_variables_label.configure(font=("Open Sans",10)) 
            self.x_variables_label=Label(self.SCREEN_POPUP,text="Indepednet Variable (X)",bg=self.bg_colour,fg=self.fg_colour) ; self.x_variables_label.grid(column=1,row=4) ; self.x_variables_label.configure(font=("Open Sans",10)) 
            self.alpha_level_label=Label(self.SCREEN_POPUP,text="Level of Significance (Alpha) (Optional)",bg=self.bg_colour,fg=self.fg_colour) ; self.alpha_level_label.grid(column=1,row=6) ; self.alpha_level_label.configure(font=("Open Sans",10)) 

    def run(self):
        if self.dropdown_test_options_logic[0][1]:
            self.run_button=Button(self.SCREEN_POPUP,text="Run",bg=self.bg_colour,fg=self.fg_colour,command=lambda:[LinearRegression.get_entry_values(self),LinearRegression.testing_window(self)]) ; self.run_button.grid(column=1,row=8,pady=10)
        
    def testing_window(self):
        LinearRegression.get_entry_values(self)
        if self.dropdown_test_options_logic[0][1]:
          self.SCREEN_TEST=Tk() ; self.SCREEN_TEST.geometry("1200x800") ; self.SCREEN_TEST.config(bg="gray0") ; self.SCREEN_TEST.title("Linear Regression Test Results") ; self.SCREEN_TEST.resizable(False,False)

home=Home(file_label,data,data_label,string,dropdown_test_options_logic)
home.text()
home.data_organization()
home.test_type()
home.confirmation_button()
home.data_clear_button()
home.next_step()

linereg=LinearRegression()
linereg.next_step_window()
linereg.next_step_window_entries()
linereg.next_step_window_labels()
linereg.get_entry_values()
linereg.run()
linereg.testing_window()

SCREEN.mainloop()