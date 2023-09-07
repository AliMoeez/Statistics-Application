import matplotlib.pyplot as plt, numpy as np, tkinter, pandas as pd
from sklearn import linear_model
import statsmodels.api as sm
import statsmodels.stats.stattools as st
import seaborn

#mock_data

df=pd.read_csv(r"C:\Users\Owner\Desktop\Data_Set_2 - Sheet1.csv")

y=df["y"]
x=df[["x_1","x_2"]]

#print(df)

#regression

reg=sm.OLS(y,sm.add_constant(x)).fit()

#print(reg.params)

list_2=[]

for i in reg.params:
    list_2.append(str(round(i,4)))

for i,y in enumerate(list_2):
    if i==0: list_2[i]=f"{y}"
    if i>0:
        if "-" in list_2[i]: list_2[i]=f"{y} x{i}"
        else: list_2[i]=f"+{y} x{i}"

combine="  ".join(list_2)

#print(f"y = {combine}")


#print(st.durbin_watson(reg.resid))

#print(reg.summary())


reg_ci=reg.conf_int(0.05)

list_4=[]

for col in df:
    list_4.append(col)

list_4[0]="const"

#print(list_4)
#print(reg_ci)
test=(round(reg_ci,4).values.tolist())

#print(test)
for i,y in enumerate(test):
     print(type(y))
     y.insert(0,list_4[i])


test_2=str(test)[1:-1]

test_2=test_2.replace("["," ")
test_2=test_2.replace("]"," ")

print(test_2)

reg_ci_1=str(round(reg_ci,4).to_dict())[1:-1][1:-1]

"""reg_betas=reg.params
reg_r_2=reg.rsquared
reg_se=reg.bse
reg_predict=reg.predict()


value=np.identity(len(reg.params))
value=value[1:,:]
reg_f_test=reg.f_test(value)
dir(reg_f_test)"""


"""reg_se_1=reg_se.to_dict()

print(str(reg_se_1)[1:-1])"""


#print(reg_ci.to_string())
#print(reg_betas.to_string())
#print(reg_r_2)
#print(reg_se.to_string())
#print("")
#print(reg_f_test.fvalue)
#print(reg_f_test.pvalue)


"""list_3=[]

for col in df:
    list_3.append(col)

reg_pvalue_name=round(reg.pvalues[0:len(list_3)],4).to_dict()

x=[str(i)+" : " + str(n) for i,n in reg_pvalue_name.items()]

print(*x)

list_1=[]"""

#for col in df:
#    if col !="y":
#        list_1.append(col)

#for col in list_1:
#    regression=np.polyfit(df[col],df["y"],1)
#    regression_line=np.poly1d(regression)
#    plt.scatter(x=df[col],y=df["y"])
#    plt.plot(df[col],regression_line(df[col]),label=col)  
#    plt.legend(loc="upper center")
#    plt.title("X1,..,Xn and Y Plotted") ; plt.xlabel("X1,...,Xn") ; plt.ylabel("Y") 

#plt.show()

    

"""x_1=df["x_1"]
x_2=df["x_2"]

regression=np.polyfit(x_1,y,1) 
regression_line=np.poly1d(regression)

regression_1=np.polyfit(x_2,y,1) 
regression_line_1=np.poly1d(regression_1)



plt.plot(x_1,regression_line(x_1),label="x_1")  
plt.plot(x_2,regression_line_1(x_2),label="x_2")
plt.legend(loc="upper center")
plt.title("X1,..,Xn and Y Plotted") ; plt.xlabel("X1,...,Xn") ; plt.ylabel("Y") 

plt.show()"""









