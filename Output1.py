import pandas as pd
df1=pd.read_csv("D:\Programming\CompanyData\Name_Mobile_data.csv")
df2=pd.read_csv("D:\Programming\CompanyData\Email_Age_data.csv")
df3=pd.DataFrame({'C-NAME':df1['Company Name'],'C-EMAIL':df2['Email'],'C-PHONE':df1['Mobile']})
df3.to_csv("D:\Programming\CompanyData\Output1.csv",index_label='S.No')
