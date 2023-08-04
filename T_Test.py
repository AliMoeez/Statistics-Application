from scipy.stats import ttest_ind
from scipy.stats import ttest_rel
import pandas as pd 

df=pd.read_csv(r"C:\Users\Owner\Desktop\Data_Set_1 - Sheet1.csv")

data_1=df["x"]
data_2=df["y"]

t_test=ttest_ind(data_1,data_2,alternative="two-sided") #t-test for independent means

#alternative may be "two-sided" (d_1=d_2), "less" (d_1<d_2), "right" (d_1>d_2)

print(t_test[0]) #test statsitics
print(t_test[1]) #p-value


t_test_rel=ttest_rel(data_1,data_2) # t-test for depedent means 

print(t_test_rel[0]) #test statsitics
print(t_test_rel[1]) #p-value


