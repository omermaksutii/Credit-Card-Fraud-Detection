import requests_html
import pandas as pd
import numpy as np
from pandas import DataFrame
df1=pd.read_csv("v1.csv")
df2=pd.read_csv("v2.csv")
df3=pd.read_csv("v3.csv")
df4=pd.read_csv("v4.csv")
df5=pd.read_csv("v5.csv")
df6=pd.read_csv("v6.csv")

dataframes=[df2,df3,df4,df5,df6]
new=[]
for x in dataframes:
    x=x.set_index('Time')
    new.append(pd.Series(x.values.tolist(),index=x.index))
dataframe=pd.concat(new,axis=1,keys=('V1','V2','V3','V4','V5','V6'),sort=True)
dataframe.to_csv("creditcard.csv")
print(dataframe)