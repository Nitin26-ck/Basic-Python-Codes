import pandas as pd
import xlrd

empdata=[(1001,'ganesh rao',110000),(1002,'harita raj',67000),(1003,'akash seth',72000),(1004,'srikanth desai',59000),(1005,'soumya agarwal',63000)]
df=pd.DataFrame(empdata,columns=["eno","ename","salary"])

print(df)
print(df.shape)
print(df[2:5])
print(df['eno'])
print(df['salary'].min())
print(df.describe())
print(df.sort_values('salary'))