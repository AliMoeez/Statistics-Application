import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf,plot_pacf
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_predict

df=pd.read_csv(r"C:\Users\Owner\Desktop\Data_Set_4 - Sheet1.csv")

#x=plt.plot(df["Time"],df["Data"])
plt.ylabel("Y")
plt.xlabel("X")

#acf=plot_acf(df["Data"])
#pacf=plot_pacf(df["Data"])

adfuller_test=adfuller(df["Data"])

print(adfuller_test[1]) #>0.05 --> that non-stationary 

df_diff=df["Data"].diff().dropna() # diffrernce data to remove non-stationarity

#df_diff.plot()

arima_model_shown=ARIMA(df["Data"],order=(1,1,1))
arima_model_fit=arima_model_shown.fit()
arima_model_fit.summary()

residuals=arima_model_fit.resid[1:]

fig,ax=plt.subplots(1,3)
residuals.plot(ax=ax[0]) #white noise reisudal are good
residuals.plot(kind="kde",ax=ax[1]) # normally distributied resudals arfe good with meam approxlmetly 0

forecast_ts=arima_model_fit.forecast(len(df["Data"]))

df["Data"].plot(ax=ax[2])

plot_predict(arima_model_fit,55,115,ax=ax[2])

plt.show()

