import pandas as pd

df=pd.read_csv(r"C:\Users\Owner\Desktop\Data_Set_1 - Sheet1.csv")

col_one="y"
col_two="x"

for col in df:
    if col in [col_one,col_two]:
        print("yes")