import matplotlib.pyplot as plt, numpy as np, tkinter, pandas as pd
from sklearn import linear_model
import statsmodels.api as sm

#mock_data

df=pd.read_csv(r"C:\Users\Owner\Desktop\Data_Set_2 - Sheet1.csv")

y=df["y"]
x=df[["x_1","x_2"]]

#regression

reg=sm.OLS(y,sm.add_constant(x)).fit()

print(reg.summary())

reg_ci=reg.conf_int(0.05)
reg_betas=reg.params
reg_r_2=reg.rsquared
reg_se=reg.bse
reg_predict=reg.predict()


value=np.identity(len(reg.params))
value=value[1:,:]
reg_f_test=reg.f_test(value)
dir(reg_f_test)

#print(reg_ci.to_string())
#print(reg_betas.to_string())
#print(reg_r_2)
#print(reg_se.to_string())
#print("")
print(reg_f_test.fvalue)
print(reg_f_test.pvalue)

list=[]

for col in df:
    list.append(col)

reg_pvalue=reg.pvalues[0:len(list)].to_string()

print(reg_pvalue)









