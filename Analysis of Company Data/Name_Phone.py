import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import time
names=[]
mobiles=[]
request=requests.get("https://www.fundoodata.com/advance_search_results.php?&company_type_id[]=2&company_type_id[]=5&company_type_id[]=3&company_type_id[]=4&company_type_id[]=1&company_type_id[]=6&company_entity_id[]=1&company_entity_id[]=2&company_entity_id[]=3&company_entity_id[]=4&level_id=1&search_type=1")
b=True
for i in range(0,100):
    soup=BeautifulSoup(request.text,features="html.parser")
    results=soup.find('div',attrs={'class':'search-page-right-pannel'})
    if results!=None:
        for a in results.findAll('div',attrs={'class':'search-result'}):
            name=a.find('div',attrs={'class':'heading'})
            if name==None:
                continue
            link=name.contents[0]
            link1=link['href']
            request1=requests.get(link1)
            soup1=BeautifulSoup(request1.text,features="html.parser")
            dl=soup1.find('div',attrs={'class':'detail-line'})
            cname=name.text.strip()
            names.append(cname)
            print("Name",cname)
            dll=dl.contents
            if len(dll) > 1 :
                mobiles.append(dll[1])
                print("Mobile",dll[1])
            else:
                mobiles.append("NA")
        res=results.find('div',attrs={'class':'alphabet-search'})
        l=[]
        for bt in res.findAll('a'):
            l.append(bt.text.strip())
        s="https://www.fundoodata.com"+bt['href']
        print(l[0],"  Form1")
        if "Next" in l:
            request=requests.get(s)
    else:
        results=soup.find('div',attrs={'class':'search-page-paid-pannel'})
        count=0
        for a in results.findAll('tr',attrs={'class':'table-search-format'}):
            name=a.find('td').find_next('td').contents[1]
            mobile=a.findAll('td')
            li=mobile[4].contents
            if name==None :
                continue
            count+=1
            if count%2 == 1:
                anc=li[0]
                cname=name.text.strip()
                names.append(cname)
                mobiles.append(anc.text.strip())
        res=results.find('div',attrs={'class':'alphabet-search paid-paging'})
        l=[]
        for bt in res.findAll('a'):
            l.append(bt.text.strip())
        s="https://www.fundoodata.com"+bt['href']
        print(l[0],"  Form2")
        if "Next" in l:
            request=requests.get(s)
    time.sleep(1)
df=pd.DataFrame({'Company Name':names,'Mobile':mobiles})
df.to_csv("D:\Programming\CompanyData\Name_Mobile_data.csv",index_label='SNo',mode='a')
