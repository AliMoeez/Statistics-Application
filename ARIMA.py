import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf,plot_pacf
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_predict
from tkinter import *
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

x=False

#SCREEN=Tk()

#SCREEN.geometry("1200x800") ; SCREEN.config(bg="gray0") ; SCREEN.title("Statistics Application") ; SCREEN.resizable(False,False)

df=pd.read_csv(r"C:\Users\Owner\Desktop\Data_Set_4 - Sheet1.csv")

#df_diff=df["Data"].diff().dropna()

df_diff=df["Data"].diff(2).dropna()

#df_new=df["Time"][:-2]

"""#x=plt.plot(df["Time"],df["Data"])
#plt.ylabel("Y")
#plt.xlabel("X")

acf=plot_acf(df["Data"])
pacf=plot_pacf(df["Data"])


figure_plot=plt.Figure(figsize=(7,4))
     #   self.figure_num=self.figure_plot.add_subplot(131)
     #   self.figure_num.plot(self.data[self.time_use_entry.get()],self.data[self.data_use_entry.get()])

figure_num=figure_plot.add_subplot(121)
figure_num.plot(data=plot_acf(df["Data"]))
#figure_num.margins(100)

figure_num=figure_plot.add_subplot(122)
figure_num.plot(df["Time"],df["Data"])

figure_show=FigureCanvasTkAgg(figure_plot,master=SCREEN)
figure_show.get_tk_widget().grid(column=1,row=1)
toolbar=NavigationToolbar2Tk(figure_show,SCREEN,pack_toolbar=False,)
toolbar.grid(column=1,row=2,pady=10)
plt.show()"""


adfuller_test=adfuller(df["Data"])

print(adfuller_test[1]) #>0.05 --> that non-stationary 

df_diff=df["Data"].diff().dropna() # diffrernce data to remove non-stationarity

#df_diff.plot()

arima_model_shown=ARIMA(df["Data"],order=(1,1,1))
arima_model_fit=arima_model_shown.fit()
arima_model_fit.summary()

residuals=arima_model_fit.resid[1:]




fig,sax=plt.subplots(1,3)
residuals.plot(ax=sax[0]) #white noise reisudal are good
residuals.plot(kind="kde",ax=sax[1]) # normally distributied resudals arfe good with meam approxlmetly 0

forecast_ts=arima_model_fit.forecast(len(df["Data"]))

df["Data"].plot(ax=sax[2])

plot_predict(arima_model_fit,55,115,ax=sax[2])

plt.show()

#SCREEN.mainloop()

