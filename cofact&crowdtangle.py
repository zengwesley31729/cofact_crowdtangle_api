#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import time 
import Post
import numpy as np
import os
#imput dataset
url= pd.read_csv('cofact_dataset_labeled.csv')

#choose data include type  rumor
rumor_link=url.loc[url['replyType']=='RUMOR']

#drop 0 or None
rumor_link = rumor_link.dropna(how='any',axis=0)

# setting output folder path
folder='C:/Users/zengwesley/My_AI_Lab/Cofact&DTL/api_result/'
output_path = os.path.join(folder,'output_data')+'.csv'
# a numer to name output csv data
i=0
#loop for all dataset
for url in rumor_link['url']:
    print(i)
    if str(url) != None:
        link=str(url)
        #call api
        data = Post.ct_link(count=1000, 
                            start_Date= "2020-01-01", 
                            end_Date="2021-07-31", 
                            include_History= None, 
                            link= link, 
                            include_Summary= None,
                            sortBy="date", 
                            searchField= None, 
                            offset = None, 
                            api_token=Post.token, 
                            platforms= 'facebook')
        #tranfor json to dataframe
        df = pd.json_normalize(data['result']['posts'])
        #set out put path
        output_path=os.path.join(folder,str(i))+'.csv'
        i=i+1
        #out put data
        df.to_csv(output_path)
        # api can only call 2 time in 1 minute
        time.sleep(35)


# In[ ]:




