import pandas as pd 

test=pd.read_csv(r"C:/Users/Owner/Downloads/Data_Set_1 - Sheet1.csv")

for idx in test.columns:
    print(idx)