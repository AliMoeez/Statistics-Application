import matplotlib.pyplot as plt, numpy as np, tkinter, pandas as pd
from sklearn import linear_model

#mock_data

#df=pd.DataFrame({'x1':[100,101,105,107,110,115,125,187],
#                 'y':[1,2,3,4,5,6,7,8]})

df=pd.read_csv(r"C:/Users/Owner/Downloads/Data_Set_1 - Sheet1.csv")

y=df["y"]
x=df["x"]

#regression

regression=np.polyfit(x,y,1)  #gets the intercept and slope
regression_line=np.poly1d(regression) #equation written in slope intecept form
regression_correlation=np.corrcoef(x,y) # correaltion coefficient
print(regression_line,"Regression Equation")
print(regression_correlation[0][1],"Correlation of X and Y")

#plot

plt.scatter(x=x,y=y) #data
plt.plot(x,regression_line(x))  #takes x and the regression line from above and plots it with the data
plt.title("X and Y Plotted") ; plt.xlabel("X") ; plt.ylabel("Y") #labels
plt.show() #show plot