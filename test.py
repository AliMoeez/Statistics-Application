import matplotlib.pyplot as plt, numpy as np, tkinter, pandas as pd

#mock_data

df=pd.DataFrame({'x':[100,101,105,107,110,115,125,187],
                 'y':[1,2,3,4,5,6,7,8]})


y=df["y"]
x=df["x"]

#regression

regression=np.polyfit(x,y,1)  #gets the intercept and slope
regression_line=np.poly1d(regression) #equation written in slope intecept form
regression_correlation=np.corrcoef(x,y) # correaltion coefficient

print(regression_line,"Regression Eqaution") #regression equation
print(regression_correlation[1][0],"Correlation Coefficient") #see that values in (2,1), (1,2) are the correl values, but can only show one value as well

#plot

plt.scatter(x=x,y=y) #data
plt.plot(x,regression_line(x))  #takes x and the regression line from above and plots it with the data
plt.title("X and Y Plotted") ; plt.xlabel("X") ; plt.ylabel("Y") #labels
#plt.show() #show plot