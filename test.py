import statsmodels.api as sm
import math
import pandas as pd 


df=pd.read_csv(r"C:/Users/Owner/Desktop/Data_Set_1 - Sheet1.csv")

y=df["y"]
x=df["x"]

regression_ols=sm.OLS(y,sm.add_constant(x)).fit()