from Output1 import df3,df2
import pandas as pd
df3['C-Age']=df2['Age']
sdf=df3[df3['C-Age']<=2.0]
sdf.drop('C-Age',axis=1,inplace=True)
print("StartUp")
print(sdf.head())
print(sdf.shape)
sdf.to_csv("D:\Programming\CompanyData\StartUp.csv",index_label='S.No')
mdf=df3[(df3['C-Age']>2.0) &  (df3['C-Age']<=8.0)]
mdf.drop('C-Age',axis=1,inplace=True)
print("Mid")
print(mdf.head())
print(mdf.shape)
mdf.to_csv("D:\Programming\CompanyData\MidLevel.csv",index_label='S.No')
edf=df3[df3['C-Age']>=10.0]
edf.drop('C-Age',axis=1,inplace=True)
print("Established")
print(edf.head())
print(edf.shape)
edf.to_csv("D:\Programming\CompanyData\Established.csv",index_label='S.No')
