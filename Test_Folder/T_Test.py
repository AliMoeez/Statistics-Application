from scipy.stats import ttest_ind
from scipy.stats import ttest_rel
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np 

df=pd.read_csv(r"C:\Users\Owner\Desktop\Data_Set_3 - Sheet1.csv")

data_1=df["x"]
data_2=df["y"]


mean_1=np.mean(data_1)
mean_2=np.mean(data_2)

std_1=np.std(data_1)
std_2=np.std(data_2)

print(mean_1)
print(mean_2)


# independnet t-test ==> tests for differences among two sepeate gruops
# dependent t-test ==> tests for differcnes among same group in different time periods 

t_test=ttest_ind(data_1,data_2,alternative="two-sided") #t-test for independent means


#alternative may be "two-sided" (d_1=d_2), "less" (d_1<d_2), "greater" (d_1>d_2)

print(t_test[0]) #test statsitics
print(t_test[1]) #p-value


t_test_rel=ttest_rel(data_1,data_2) # t-test for dependent means 

print(t_test_rel[0]) #test statsitics
print(t_test_rel[1]) #p-value

list=[df.columns]

print(list)

plt.bar(list[0][1],mean_1,yerr=std_1,capsize=10)
plt.bar(list[0][0],mean_2,yerr=std_2,capsize=10)
plt.show()


