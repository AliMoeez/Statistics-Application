import matplotlib.pyplot as plt, numpy as np, tkinter, pandas as pd
from sklearn import linear_model

#mock_data

df=pd.DataFrame({'x1':[100,101,105,107,110,115,125,187],
                 'x2':[120,124,123,124,192,125,127,129],
                 'y':[1,2,3,4,5,6,7,8]})


y=df["y"]
x=df[["x1","x2"]]

#regression

regression=linear_model.LinearRegression()

reg=regression.fit(df[["x1","x2"]],df["y"])

print(reg.coef_)
print(reg.intercept_)