import matplotlib.pyplot as plt, numpy as np, pandas as pd
from sklearn import linear_model
import statsmodels.api as sm
from tkinter import *
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from scipy.stats import ttest_ind, ttest_rel

SCREEN=Tk()

SCREEN.geometry("1200x800") ; SCREEN.config(bg="gray0") ; SCREEN.title("Statistics Application") ; SCREEN.resizable(False,False)

file_label="" ; data="" ; data_label="" ; string="TEST" ; dropdown_test_options_logic=[(0,0),(0,0),(0,0),(0,0)]

line_reg_model=False
mult_reg_model=False
ttest_model=False
ARIMA_model=False

show_linear_regression=False
show_ttest=False
show_multiple_regression=False

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
        self.next_button=Button(SCREEN,text="Next",bg=self.bg_colour,fg=self.fg_colour,command=lambda:[Home.confirmation_button(self),LinearRegression.next_step_window(self),TTest.next_step_window(self),MultipleRegression.next_step_window(self)]) 
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
        global show_linear_regression
        self.col_list=[0]
        if self.dropdown_test_options_logic[0][1]:                        
            self.error_input_text=Label(self.SCREEN_POPUP,text="",fg=self.fg_colour,bg=self.bg_colour) ; self.error_input_text.grid(column=1,row=9) ; self.error_input_text.configure(font=("Open Sans",10))  ; show_linear_regression=False
            for col in self.data:
                if col in [self.y_variables_entry.get(),self.x_variables_entry.get()]:
                    self.col_list[0]+=1
                if self.col_list[0]>=len([self.y_variables_entry.get(),self.x_variables_entry.get()]) and float(self.alpha_level_entry.get()):
                    show_linear_regression=True ; self.error_input_text.configure(text="")
                else:
                    self.error_input_text.configure(text="ERROR: Check Your Input Boxes (Y,X,Alpha) For Invalid Inputs.")  ; show_linear_regression=False

    def next_step_window_labels(self):
        if self.dropdown_test_options_logic[0][1]:
            self.placeholder_text=Label(self.SCREEN_POPUP,text="",fg=self.fg_colour,bg=self.bg_colour) ; self.placeholder_text.grid(column=0,row=0,padx=70)
            self.linereg_text=Label(self.SCREEN_POPUP,text="Enter Your Parameters Below",fg=self.fg_colour,bg=self.bg_colour) ; self.linereg_text.grid(column=1,row=0) ; self.linereg_text.configure(font=("Open Sans",18)) 
            self.y_variables_label=Label(self.SCREEN_POPUP,text="Dependent Variable (Y)",bg=self.bg_colour,fg=self.fg_colour) ; self.y_variables_label.grid(column=1,row=2) ; self.y_variables_label.configure(font=("Open Sans",10)) 
            self.x_variables_label=Label(self.SCREEN_POPUP,text="Indepednet Variable (X)",bg=self.bg_colour,fg=self.fg_colour) ; self.x_variables_label.grid(column=1,row=4) ; self.x_variables_label.configure(font=("Open Sans",10)) 
            self.alpha_level_label=Label(self.SCREEN_POPUP,text="Level of Significance (Alpha)",bg=self.bg_colour,fg=self.fg_colour) ; self.alpha_level_label.grid(column=1,row=6) ; self.alpha_level_label.configure(font=("Open Sans",10)) 

    def run(self):
        if self.dropdown_test_options_logic[0][1]:
            self.run_button=Button(self.SCREEN_POPUP,text="Run",bg=self.bg_colour,fg=self.fg_colour,command=lambda:[LinearRegression.get_entry_values(self),LinearRegression.testing_window(self)]) ; self.run_button.grid(column=1,row=8,pady=10)
        
    def testing_window(self):
        global show_linear_regression
        LinearRegression.get_entry_values(self)
        if self.dropdown_test_options_logic[0][1] and show_linear_regression:
            self.SCREEN_TEST=Tk() ; self.SCREEN_TEST.geometry("1200x800") ; self.SCREEN_TEST.config(bg="gray0") ; self.SCREEN_TEST.title("Linear Regression Test Results") ; self.SCREEN_TEST.resizable(False,False)
            LinearRegression.testing_window_labels(self)
            LinearRegression.testing_graph(self)
            LinearRegression.testing_statistics(self)

    def testing_window_labels(self):
        if self.dropdown_test_options_logic[0][1] and show_linear_regression:
            self.alpha_level=float(self.alpha_level_entry.get())
            self.blank_label=Label(self.SCREEN_TEST,text="",fg=self.fg_colour,bg=self.bg_colour) ; self.blank_label.grid(column=0,row=0,padx=180)
            self.title_label=Label(self.SCREEN_TEST,text="Linear Regression Output",fg=self.fg_colour,bg=self.bg_colour) ;  self.title_label.grid(column=1,row=0) ; self.title_label.configure(font=("Open Sans",25))
            self.regression_betas_f_p_value_label_title=Label(self.SCREEN_TEST,text=f"Regression Beta P-Values",bg=self.bg_colour,fg=self.fg_colour)  ; self.regression_betas_f_p_value_label_title.grid(column=1,row=3) ; self.regression_betas_f_p_value_label_title.configure(font=("Open Sans",10,'bold')) 
            self.test_ci_label=Label(self.SCREEN_TEST,text=f"{round((1-self.alpha_level)*100,0)}% Confidence Interval For Beta's",fg=self.fg_colour,bg=self.bg_colour) ; self.test_ci_label.grid(column=1,row=11)  ; self.test_ci_label.configure(font=("Open Sans",10,'bold'))

    def testing_graph(self):
        if self.dropdown_test_options_logic[0][1] and show_linear_regression:
            try:
                plt.style.use("dark_background") 
                self.dependent_variable=self.data[self.y_variables_entry.get()]  ; self.independent_variable=self.data[self.x_variables_entry.get()]
                self.figure=plt.Figure(figsize=(5,4),dpi=100)  ; self.figure_plot=self.figure.add_subplot(111)  ; self.figure.subplots_adjust(bottom=0.193)

                self.regression=np.polyfit(self.independent_variable,self.dependent_variable,1) ; self.regression_plot=np.poly1d(self.regression)
                self.figure_plot.scatter(x=self.independent_variable,y=self.dependent_variable)  ; self.figure_plot.plot(self.independent_variable,self.regression_plot(self.independent_variable))

                self.regression_plot=FigureCanvasTkAgg(self.figure,self.SCREEN_TEST) ; self.regression_plot.get_tk_widget().grid(column=1,row=1)
                self.toolbar=NavigationToolbar2Tk(self.regression_plot,self.SCREEN_TEST,pack_toolbar=False,) 
                self.toolbar.update() 
                self.toolbar.grid(column=1,row=1,sticky='s')
            except KeyError : pass

    def testing_statistics(self):
        if self.dropdown_test_options_logic[0][1] and show_linear_regression:
            try:
                self.dependent_variable=self.data[self.y_variables_entry.get()]
                self.independent_variable=self.data[self.x_variables_entry.get()]
                self.alpha_level=float(self.alpha_level_entry.get())
                self.list_length=[]
                for col in self.data: self.list_length.append(col)
                
                self.regression_coefficients=np.polyfit(self.independent_variable,self.dependent_variable,1)
                self.regression_equation=np.poly1d(self.regression_coefficients)
                self.regression_ols=sm.OLS(self.dependent_variable,sm.add_constant(self.independent_variable)).fit()
                self.regression_f_test=self.regression_ols.f_test([0,1]) ; dir(self.regression_f_test)
                self.regression_f_value=self.regression_f_test.fvalue ; self.regression_p_value=self.regression_f_test.pvalue
                self.regression_r_2=self.regression_ols.rsquared
                self.regression_se=self.regression_ols.bse
                self.regression_predict=self.regression_ols.predict()

                self.regression_f_p_value_label=Label(self.SCREEN_TEST,text=f"F-Value: {round(self.regression_f_value,4)} -- p-value: {round(self.regression_p_value,4)}",bg=self.bg_colour,fg=self.fg_colour)  ; self.regression_f_p_value_label.grid(column=1,row=2,pady=10) ; self.regression_f_p_value_label.configure(font=("Open Sans",10,'bold')) 
                self.regression_betas_f_p_value_label=Label(self.SCREEN_TEST,text=f"{round(self.regression_ols.pvalues[0:len(self.list_length)],4).to_string()}",bg=self.bg_colour,fg=self.fg_colour)  ; self.regression_betas_f_p_value_label.grid(column=1,row=4) ; self.regression_betas_f_p_value_label.configure(font=("Open Sans",10)) #(1,4)
                self.regression_equation_label=Label(self.SCREEN_TEST,text=f"Regression Equation: {str(self.regression_equation)}",bg=self.bg_colour,fg=self.fg_colour) ; self.regression_equation_label.grid(column=1,row=6) ; self.regression_equation_label.configure(font=("Open Sans",10,'bold')) 
                self.regression_r_2_label=Label(self.SCREEN_TEST,text=f"R-Sqaured: {round(self.regression_r_2,4)}",bg=self.bg_colour,fg=self.fg_colour) ; self.regression_r_2_label.grid(column=1,row=7) ; self.regression_r_2_label.configure(font=("Open Sans",10,'bold')) 
                self.test_ci_label_values=Label(self.SCREEN_TEST,text=self.regression_ols.conf_int(1-self.alpha_level),fg=self.fg_colour,bg=self.bg_colour) ; self.test_ci_label_values.grid(column=1,row=12) ; self.test_ci_label_values.configure(font=("Open Sans",10))
                
                if self.regression_p_value<=0.05:
                    self.conclusion_label=Label(self.SCREEN_TEST,text=f"Since {self.regression_p_value} <= 0.05, we can say that this model is a good predictor of {self.y_variables_entry.get()}",fg=self.fg_colour,bg=self.bg_colour) ; self.conclusion_label.grid(column=1,row=13) ; self.conclusion_label.configure(font=("Open Sans",10))
                if self.regression_p_value>0.05:
                    self.conclusion_label=Label(self.SCREEN_TEST,text=f"Since {round(self.regression_p_value,4)} > 0.05, we can say that this model is a not a good predictor of {self.y_variables_entry.get()}",fg=self.fg_colour,bg=self.bg_colour) ; self.conclusion_label.grid(column=1,row=13) ; self.conclusion_label.configure(font=("Open Sans",10))
            except AttributeError: pass

class TTest(Home):
    def __init__(self):
        super().__init__(file_label,data,data_label,string,dropdown_test_options_logic) 
        self.dropdown_test_options_logic=dropdown_test_options_logic
    
    def next_step_window(self):
        global ttest_model
        if self.dropdown_test_options_logic[2][1]:
            self.SCREEN_POPUP=Tk() ; self.SCREEN_POPUP.geometry("600x300") ; self.SCREEN_POPUP.config(bg=self.bg_colour) ; self.SCREEN_POPUP.title("T-Test Settings") ; self.SCREEN_POPUP.resizable(False,False)
            TTest.next_step_window_entries(self)
            TTest.next_step_window_labels(self)
            TTest.run(self)

    def next_step_window_entries(self):
        if self.dropdown_test_options_logic[2][1]:
            self.data_1_values=Entry(self.SCREEN_POPUP) ; self.data_1_values.grid(column=1,row=3) ; self.data_1_values.config(bg=self.bg_colour, fg=self.fg_colour)
            self.data_2_values=Entry(self.SCREEN_POPUP) ; self.data_2_values.grid(column=1,row=5) ; self.data_2_values.config(bg=self.bg_colour, fg=self.fg_colour)
            self.sided_values=Entry(self.SCREEN_POPUP) ; self.sided_values.grid(column=1,row=7) ; self.sided_values.config(bg=self.bg_colour, fg=self.fg_colour)
            self.test_type_values=Entry(self.SCREEN_POPUP) ; self.test_type_values.grid(column=1,row=9) ; self.test_type_values.config(bg=self.bg_colour, fg=self.fg_colour)

    def next_step_window_labels(self):
        if self.dropdown_test_options_logic[2][1]:
            self.placeholder_text=Label(self.SCREEN_POPUP,text="",fg=self.fg_colour,bg=self.bg_colour) ; self.placeholder_text.grid(column=0,row=0,padx=30)
            self.ttest_test=Label(self.SCREEN_POPUP,text="Enter Your Parameters Below",fg=self.fg_colour,bg=self.bg_colour) ; self.ttest_test.grid(column=1,row=0) ; self.ttest_test.configure(font=("Open Sans",15)) 
            self.data_1_values_labels=Label(self.SCREEN_POPUP,text="Sample One",bg=self.bg_colour,fg=self.fg_colour) ; self.data_1_values_labels.grid(column=1,row=2) ; self.data_1_values_labels.configure(font=("Open Sans",10)) 
            self.data_2_values_labels=Label(self.SCREEN_POPUP,text="Sample Two",bg=self.bg_colour,fg=self.fg_colour) ; self.data_2_values_labels.grid(column=1,row=4) ; self.data_2_values_labels.configure(font=("Open Sans",10)) 
            self.sided_values_labels=Label(self.SCREEN_POPUP,text="Tails (1= Two-Sided, 0= Sample One > Sample Two, -1= Sample One < Sample Two)",bg=self.bg_colour,fg=self.fg_colour) ; self.sided_values_labels.grid(column=1,row=6) ; self.sided_values_labels.configure(font=("Open Sans",10)) 
            self.test_type_labels=Label(self.SCREEN_POPUP,text="Test Type (1= Independent Sample, 0= Dependent Sample)",bg=self.bg_colour,fg=self.fg_colour) ; self.test_type_labels.grid(column=1,row=8) ; self.test_type_labels.configure(font=("Open Sans",10)) 

    def get_entry_values(self):
        global show_ttest
        if self.dropdown_test_options_logic[2][1]:
            self.col_list=[0]                     
            self.error_input_text=Label(self.SCREEN_POPUP,text="",fg=self.fg_colour,bg=self.bg_colour) ; self.error_input_text.grid(column=1,row=11) ; self.error_input_text.configure(font=("Open Sans",10))  ; show_linear_regression=False
            for col in self.data:
                if col in [self.data_1_values.get(),self.data_2_values.get()]:
                    self.col_list[0]+=1
                if self.col_list[0]>=len([self.data_1_values.get(),self.data_2_values.get()]) and self.sided_values.get() in ["1","0","-1"] and self.test_type_values.get() in ["0","1"]:
                    show_ttest=True ; self.error_input_text.configure(text="")
                else:
                    self.error_input_text.configure(text="ERROR: Check Your Input Boxes For Invalid Inputs.")  ; show_ttest=False
    
    def run(self):
        if self.dropdown_test_options_logic[2][1]:
            self.run_button=Button(self.SCREEN_POPUP,text="Run",bg=self.bg_colour,fg=self.fg_colour,command=lambda:[TTest.get_entry_values(self),TTest.testing_window(self)]) ; self.run_button.grid(column=1,row=10,pady=10)

    def testing_window(self):
        global show_ttest
        TTest.get_entry_values(self)
        if self.dropdown_test_options_logic[2][1] and show_ttest:
            self.SCREEN_TEST=Tk() ; self.SCREEN_TEST.geometry("1200x800") ; self.SCREEN_TEST.config(bg="gray0") ; self.SCREEN_TEST.title("T-Test Test Results") ; self.SCREEN_TEST.resizable(False,False)
            TTest.testing_window_labels(self)
            TTest.testing_window_graph(self)
            TTest.testing_window_statistics(self)
        
    def testing_window_labels(self):
        if self.dropdown_test_options_logic[2][1]:
            TTest.sided_value_conversion(self)
            self.holder_label=Label(self.SCREEN_TEST,text="",fg=self.fg_colour,bg=self.bg_colour) ; self.holder_label.grid(column=0,row=0,padx=185)
            self.title_label=Label(self.SCREEN_TEST,text="T-Test Output",fg=self.fg_colour,bg=self.bg_colour) ; self.title_label.configure(font=("Open Sans",25)) ; self.title_label.grid(column=1,row=0,pady=25)
            self.test_type_string=[""]
            if self.test_type_values.get()=="1": self.test_type_string[0]="Independent"
            if self.test_type_values.get()=="0": self.test_type_string[0]="Dependent"    
            if self.sided_values.get()=="1":
                self.test_explanation_label=Label(self.SCREEN_TEST,text=f"{self.sided_list[0].title()} T-Test with {self.test_type_string[0]} Samples",fg=self.fg_colour,bg=self.bg_colour) ; self.test_explanation_label.configure(font=("Open Sans",10)); self.test_explanation_label.grid(column=1,row=2) 
            if self.sided_values.get() in ["0","-1"]:
                self.test_explanation_label=Label(self.SCREEN_TEST,text=f"T-Test where Sample One is {self.sided_list[0]} than Sample Two with {self.test_type_string[0]} Samples",fg=self.fg_colour,bg=self.bg_colour) ; self.test_explanation_label.configure(font=("Open Sans",10)); self.test_explanation_label.grid(column=1,row=2)
            self.null_hypothesis_label=Label(self.SCREEN_TEST,text=f"Ho: \u03bc0=\u03bc1",fg=self.fg_colour,bg=self.bg_colour) ; self.null_hypothesis_label.configure(font=("Open Sans",10)); self.null_hypothesis_label.grid(column=1,row=3) 
            self.alternative_hypothesis_label=Label(self.SCREEN_TEST,text=f"Ha: \u03bc0{self.sided_list_sign[0]}\u03bc1",fg=self.fg_colour,bg=self.bg_colour) ; self.alternative_hypothesis_label.configure(font=("Open Sans",10)); self.alternative_hypothesis_label.grid(column=1,row=4) 

    def testing_window_graph(self):
        if self.dropdown_test_options_logic[2][1]:
            plt.style.use("dark_background")
            self.figure_canvas=plt.Figure(figsize=(5,4),dpi=100)
            self.figure_plot=self.figure_canvas.add_subplot(111)
            self.figure_canvas.subplots_adjust(bottom=0.18)
            self.figure_canvas.subplots_adjust(top=1.00)

            self.sample_data_1=self.data[self.data_1_values.get()]
            self.sample_data_2=self.data[self.data_2_values.get()]

            self.sample_data_1_mean=np.mean(self.sample_data_1)
            self.sample_data_2_mean=np.mean(self.sample_data_2)

            self.sample_data_1_std=np.std(self.sample_data_1)
            self.sample_data_2_std=np.std(self.sample_data_2)

            self.figure_plot.bar(self.data_1_values.get(),self.sample_data_1_mean,yerr=self.sample_data_1_std,capsize=10,error_kw=dict(ecolor="grey"))
            self.figure_plot.bar(self.data_2_values.get(),self.sample_data_2_mean,yerr=self.sample_data_2_std,capsize=10,error_kw=dict(ecolor="grey"))

            self.figure=FigureCanvasTkAgg(self.figure_canvas,self.SCREEN_TEST)
            self.figure.get_tk_widget().grid(column=1,row=1)

            self.toolbar=NavigationToolbar2Tk(self.figure,self.SCREEN_TEST,pack_toolbar=False,)
            self.toolbar.update()
            self.toolbar.grid(column=1,row=1,sticky="s")

    def sided_value_conversion(self):
        ["1","0","-1"] # 1=Tw-sided , 0 =sample_1>sample_2 , -1=sample_1<sample_2
        if self.dropdown_test_options_logic[2][1]:
            self.sided_list=[""] ; self.sided_list_sign=[""]
            if self.sided_values.get()=="1":
                self.sided_list[0]="two-sided" ; self.sided_list_sign[0]="<>"
            if self.sided_values.get()=="0":
                self.sided_list[0]="greater" ; self.sided_list_sign[0]=">"
            if self.sided_values.get()=="-1":
                self.sided_list[0]="less" ; self.sided_list_sign[0]="<"

    def testing_window_statistics(self):
        TTest.sided_value_conversion(self)
        if self.dropdown_test_options_logic[2][1]:
            if self.test_type_values.get()=="1":#indepdent
               self.t_test_stats=ttest_ind(self.sample_data_1,self.sample_data_2,alternative=self.sided_list[0])
            if self.test_type_values.get()=="0":#depedent
                self.t_test_stats=ttest_rel(self.sample_data_1,self.sample_data_1,alternative=self.sided_list[0]) 
            self.t_stat_label=Label(self.SCREEN_TEST,text=f'T-Statistic {round(self.t_test_stats[0],4)} -- p-value {round(self.t_test_stats[1],4)}',fg=self.fg_colour,bg=self.bg_colour)
            self.t_stat_label.configure(font=("Open Sans",10,'bold')) ; self.t_stat_label.grid(column=1,row=5)

            self.summary_statistics_label_1=Label(self.SCREEN_TEST,text=f'Mean 1 = {round(self.sample_data_1_mean,2)} -- Std 1 = {round(self.sample_data_1_std,2)}',fg=self.fg_colour,bg=self.bg_colour)
            self.summary_statistics_label_1.configure(font=("Open Sans",10)) ; self.summary_statistics_label_1.grid(column=1,row=6)

            self.summary_statistics_label_2=Label(self.SCREEN_TEST,text=f'Mean 2 = {round(self.sample_data_2_mean,2)} -- Std 2 = {round(self.sample_data_2_std,2)}',fg=self.fg_colour,bg=self.bg_colour)
            self.summary_statistics_label_2.configure(font=("Open Sans",10)) ; self.summary_statistics_label_2.grid(column=1,row=7)
           
            if self.t_test_stats[1]>0.05:
                self.test_conclusion_label=Label(self.SCREEN_TEST,text=f'Since p-value({round(self.t_test_stats[1],4)}) > 0.05, we can say that their is not a significant difference in the means',fg=self.fg_colour, bg=self.bg_colour)
                self.test_conclusion_label.configure(font=("Open Sans",10,'bold')) ; self.test_conclusion_label.grid(column=1,row=8)
            if self.t_test_stats[1]<=0.05:
                self.test_conclusion_label=Label(self.SCREEN_TEST,text=f'Since p-value({round(self.t_test_stats[1],4)}) <= 0.05, we can say that their is a significant difference in the means',fg=self.fg_colour, bg=self.bg_colour)
                self.test_conclusion_label.configure(font=("Open Sans",10,'bold')) ; self.test_conclusion_label.grid(column=1,row=8)

class MultipleRegression(Home):
    def __init__(self):
        super().__init__(file_label,data,data_label,string,dropdown_test_options_logic)
        self.dropdown_test_options_logic=dropdown_test_options_logic

    def next_step_window(self):
        global mulreg_model
        if self.dropdown_test_options_logic[1][1]:
            self.SCREEN_POPUP=Tk() ; self.SCREEN_POPUP.geometry("600x450") ; self.SCREEN_POPUP.config(bg=self.bg_colour) ; self.SCREEN_POPUP.title("Multiple Regression Settings") ; self.SCREEN_POPUP.resizable(False,False)
            MultipleRegression.next_step_window_labels(self)
            MultipleRegression.next_step_window_checkbox(self)
            MultipleRegression.run(self)

    def next_step_window_labels(self):
        if self.dropdown_test_options_logic[1][1]:
            self.placeholder_text=Label(self.SCREEN_POPUP,text="",fg=self.fg_colour,bg=self.bg_colour) ; self.placeholder_text.grid(column=0,row=0,padx=75)
            self.param_label=Label(self.SCREEN_POPUP,text="Enter Your Parameters Below",fg=self.fg_colour,bg=self.bg_colour) ; self.param_label.grid(column=1,row=1) ; self.param_label.configure(font=("Open Sans",18)) 
            self.dep_label=Label(self.SCREEN_POPUP,text="Dependent Variable (Y)",fg=self.fg_colour,bg=self.bg_colour) ; self.dep_label.grid(column=1,row=2) ; self.dep_label.configure(font=("Open Sans",10)) 
            self.ind_label=Label(self.SCREEN_POPUP,text="Independent Variables (X1,X2,..,Xn)",fg=self.fg_colour,bg=self.bg_colour) ; self.ind_label.grid(column=1,row=4) ; self.ind_label.configure(font=("Open Sans",10)) 

    def next_step_window_checkbox(self):
        if self.dropdown_test_options_logic[1][1]:
            self.dependent_variable_entry=Entry(self.SCREEN_POPUP,fg=self.fg_colour,bg=self.bg_colour)  ; self.dependent_variable_entry.grid(column=1,row=3)
            self.multiple_select=Listbox(self.SCREEN_POPUP,selectmode=MULTIPLE,fg=self.fg_colour,bg=self.bg_colour) ; self.multiple_select.grid(column=1,row=5)
            for idx,number in enumerate(self.data):
                self.multiple_select.insert(END,number)

            self.alpha_level_label=Label(self.SCREEN_POPUP,text="Level Of Significance (Alpha)",fg=self.fg_colour,bg=self.bg_colour) ; self.alpha_level_label.grid(column=1,row=6) ; self.alpha_level_label.configure(font=("Open Sans",10)) 
            self.alpha_level_entry=Entry(self.SCREEN_POPUP,fg=self.fg_colour,bg=self.bg_colour) ; self.alpha_level_entry.grid(column=1,row=7)

    def get_entry_values(self):
        global show_multiple_regression
        if self.dropdown_test_options_logic[1][1]:
            self.col_list=[0]                  
            self.error_input_text=Label(self.SCREEN_POPUP,text="",fg=self.fg_colour,bg=self.bg_colour) ; self.error_input_text.grid(column=1,row=9) ; self.error_input_text.configure(font=("Open Sans",10)) 
            self.x_value_list=[self.multiple_select.get(idx) for idx in self.multiple_select.curselection()]
            for col in self.data:
                if col in [self.dependent_variable_entry.get()]:
                    self.col_list[0]+=1
                try:
                    if self.col_list[0]>=len([self.dependent_variable_entry.get()]) and self.dependent_variable_entry.get() not in self.x_value_list and float(self.alpha_level_entry.get()):
                        show_multiple_regression=True ; self.error_input_text.configure(text="")
                    else:
                        self.error_input_text.configure(text="ERROR: Check Your Y,X1,...,Xn,Alpha For Invalid Inputs.")  ; show_multiple_regression=False
                except ValueError: pass

    def run(self):
        if self.dropdown_test_options_logic[1][1]:
            self.run_button=Button(self.SCREEN_POPUP,text="Run",fg=self.fg_colour,bg=self.bg_colour,command=lambda:[MultipleRegression.get_entry_values(self),MultipleRegression.testing_window(self)])
            self.run_button.grid(column=1,row=8,pady=10)

    def testing_window(self):
        global show_multiple_regression
        if self.dropdown_test_options_logic[1][1] and show_multiple_regression:
            self.SCREEN_TEST=Tk() ; self.SCREEN_TEST.geometry("1200x800") ; self.SCREEN_TEST.config(bg="gray0") ; self.SCREEN_TEST.title("Multiple Regression Test Results") ; self.SCREEN_TEST.resizable(False,False)
            MultipleRegression.testing_window_labels(self)
            MultipleRegression.testing_window_graph(self)
            MultipleRegression.testing_statistics(self)

    def testing_window_labels(self):
        if self.dropdown_test_options_logic[1][1]:
            self.holder_label=Label(self.SCREEN_TEST,text="",fg=self.fg_colour,bg=self.bg_colour) ; self.holder_label.grid(column=0,row=0,padx=200)
            self.title_label=Label(self.SCREEN_TEST,text="Multiple Regression Output",fg=self.fg_colour,bg=self.bg_colour) ; self.title_label.configure(font=("Open Sans",25)) ; self.title_label.grid(column=1,row=0,pady=25)
            self.regression_f_p_values_label=Label(self.SCREEN_TEST,text="Regression F-Value & p-value (Test For All Beteas <> 0)",fg=self.fg_colour,bg=self.bg_colour) ; self.regression_f_p_values_label.grid(column=1,row=3)

    def testing_window_graph(self):
        if self.dropdown_test_options_logic[1][1]:
            plt.style.use("dark_background")
            self.fig=plt.Figure(figsize=(5,4),dpi=100)
            self.figure_regression=self.fig.add_subplot(111)
            self.x_values_graph_list=[]
            for col in self.data:
                if col!=self.dependent_variable_entry.get():
                    self.x_values_graph_list.append(col)
            for col in self.x_values_graph_list:
                regression=np.polyfit(self.data[col],self.data[self.dependent_variable_entry.get()],1)
                regression_line=np.poly1d(regression)
                self.figure_regression.scatter(x=self.data[col],y=self.data[self.dependent_variable_entry.get()])
                self.figure_regression.plot(self.data[col],regression_line(self.data[col]),label=col)  
                self.figure_regression.legend(loc="upper center")
                self.fig.suptitle("X1,..,Xn and Y Plotted") ; self.figure_regression.set_xlabel("X1,...,Xn") ; self.figure_regression.set_ylabel("Y") 
            self.figure_regression=FigureCanvasTkAgg(self.fig,master=self.SCREEN_TEST)
            self.figure_regression.get_tk_widget().grid(column=1,row=1)
            self.toolbar=NavigationToolbar2Tk(self.figure_regression,self.SCREEN_TEST,pack_toolbar=False,)
            self.toolbar.grid(column=1,row=2,pady=10)

    def testing_statistics(self):
        if self.dropdown_test_options_logic[1][1]:
            self.regression_ols=sm.OLS(self.data[self.dependent_variable_entry.get()],sm.add_constant(self.data[self.x_values_graph_list])).fit()
            self.identities=np.identity(len(self.regression_ols.params)) ; self.identities=self.identities[1:,:] ; self.reg_f_test=self.regression_ols.f_test(self.identities)    
            dir(self.reg_f_test) ; self.f_value=self.reg_f_test.fvalue ; self.p_value=self.reg_f_test.pvalue
            self.regression_f_p_values=Label(self.SCREEN_TEST,text=f"F-Value = {round(self.f_value,4)} -- p-value = {round(self.p_value,4)}",fg=self.fg_colour,bg=self.bg_colour) ; self.regression_f_p_values.grid(column=1,row=4)
            
            





            print(self.regression_ols.summary())

        

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

ttest=TTest()
ttest.next_step_window()
ttest.next_step_window_entries()
ttest.next_step_window_labels()
ttest.get_entry_values()
ttest.run()
ttest.testing_window()

mulreg=MultipleRegression()
mulreg.next_step_window()
mulreg.next_step_window_checkbox()
mulreg.next_step_window_labels()
mulreg.get_entry_values()
mulreg.run()

SCREEN.mainloop()