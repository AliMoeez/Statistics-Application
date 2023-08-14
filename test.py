import pandas as pd

df=pd.read_csv(r"C:\Users\Owner\Desktop\Data_Set_1 - Sheet1.csv")

col_one="y"
col_two="x"

number=[0]

for col in df:
    if col in [col_one,col_two]:
        number[0]+=1
    if number[0]>=len([col_one,col_two]):
        print("JHERE")
        

