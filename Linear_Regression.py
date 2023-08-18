import matplotlib.pyplot as plt, numpy as np, tkinter, pandas as pd
from sklearn import linear_model
import statsmodels.api as sm
import math


df=pd.read_csv(r"C:/Users/Owner/Desktop/Data_Set_1 - Sheet1.csv")

y=df["y"]
x=df["x"]

#regression

regression=np.polyfit(x,y,1)  #gets the intercept and slope
regression_line=np.poly1d(regression) #equation written in slope intecept form
regression_correlation=np.corrcoef(x,y) # correaltion coefficient

print(regression)
print(regression_line)

print("")

regression_ols=sm.OLS(y,sm.add_constant(x)).fit()

regression_ci=regression_ols.conf_int(0.05)
regression_betas=regression_ols.params
regression_r_2=regression_ols.rsquared
regression_se=regression_ols.bse
regression_predict=regression_ols.predict()
regression_f_test=regression_ols.f_test([0,1])
dir(regression_f_test)

print(regression_ci)
print(regression_betas)
print(regression_r_2)
print(regression_se)
print(regression_predict)
print(regression_f_test.fvalue)
print(regression_f_test.pvalue)

print(regression_line,"Regression Equation")
#print(regression_correlation[0][1],"Correlation of X and Y")

#plot

plt.scatter(x=x,y=y) #data
plt.plot(x,regression_line(x))  #takes x and the regression line from above and plots it with the data
plt.title("X and Y Plotted") ; plt.xlabel("X") ; plt.ylabel("Y") #labels
plt.show() #show plot