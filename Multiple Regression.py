import matplotlib.pyplot as plt, numpy as np, tkinter, pandas as pd
from sklearn import linear_model

#mock_data

df=pd.read_csv(r"C:\Users\Owner\Desktop\Data_Set_2 - Sheet1.csv")

y=df["y"]
x=df[["x_1","x_2"]]

#regression

regression=linear_model.LinearRegression()

reg=regression.fit(x,y)

print(reg.coef_, "Regression Coefficient")
print(reg.intercept_,"Regression Intercept")