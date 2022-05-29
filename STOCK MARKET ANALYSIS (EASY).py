#!/usr/bin/env python
# coding: utf-8

# # Stock Market Analysis
# Problem Statement: Stock market prediction and analysis are some of the most difficult jobs to complete. There are numerous causes for this, including market volatility and a variety of other dependent and independent variables that influence the value of a certain stock in the market. These variables make it extremely difficult for any stock market expert to anticipate the rise and fall of the market with great precision.

# # Data Description: About the Variables Information
# Open: The price of the stock when the market opens in the morning
# 
# Close: The price of the stock when the market closed in the evening for the day(last buy-sell orders executed between 2 traders)
# 
# High: Highest price the stock reached during that day ()
# 
# Low: Lowest price the stock is traded on that day ()
# 
# Volume: The total amount of stocks traded on that day (Total amount of Trading/Shares activity during that day/a period of Time)
# 

# # Importing Data From Website ( data Scraping)

# In[2]:


get_ipython().system('pip install datareader')


# In[3]:


get_ipython().system('pip install nsepy')


# In[4]:


import pandas_datareader.data as pdr


# In[5]:


import pandas as pd


# In[6]:


import numpy as np


# In[7]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[8]:


import seaborn as sn


# In[9]:


import datetime


# In[10]:


start= datetime.datetime(2016,1,1)


# In[11]:


end=datetime.datetime(2021,12,31)


# In[12]:


tcs=pdr.DataReader("TCS.NS",'yahoo',start,end)


# In[13]:


tcs.head()


# In[14]:


tcs.info


# # Exploratory Data Analysis

# In[15]:


tcs['Close'].plot(label='TCS Close Price',figsize=(15,7))
plt.title("Tcs Stock Prices")
plt.ylabel("Stock Price")


# In[16]:


tcs['Close'].hist(bins=50,facecolor='red',edgecolor='black')
plt.ylabel('Tcs Close Price')
plt.xlabel('Tcs Time Period')


# In[17]:


sn.distplot(tcs['Close'])


# In[18]:


tcs['Close'].plot(label='TCS Close Price',figsize=(15,7))
tcs['Open'].plot(label='TCS Open Price',figsize=(15,7))
plt.title("Tcs Stock Prices")
plt.ylabel("Stock Price")
plt.legend()


# # Plot Summary:
# As we see in graphs of open and close stocks, we see that TCS has taking many up and downs almost the whole journey.
# It start from around 2450 points and faced major down fall but at last it reached higher to 3700 points.
# We have Irregular/ Random/ Noise Component, Due to Random variation or unforseen events

# In[19]:


tcs['Close'].argmax()


# # Skewness of Close and Open Stock Prices distribution

# In[20]:


sn.jointplot(x = 'Close', y = 'Open', data = tcs, kind = 'reg',fit_reg= True,size=12)
plt.ylabel('Price')
plt.show()


# In[21]:


sn.jointplot(x = 'Close', y = 'Open', data = tcs, kind='kde')
plt.show()


# # Above Recap 1:
# We take the dataset tcs_df.csv from which we get the symbol, open and close price, date
# 
# We Converted csv to the DataFrame Format
# 
# and plot the graph of company open and close price
# 
# We Checked for the Skewness of Open and Close Stock Prices

# In[22]:


tcs.isna()


# # Above Data set we can see there is no Null Value or Missing Value

# In[23]:


tcs.plot(kind='box',label='TCS DATA VISUALIZATION',figsize=(20,10));
plt.title("TCS DATA")


# In[35]:


plt.boxplot(tcs['Volume'])
plt.ylabel('close')


# In[36]:


tcs.head()


# In[37]:


tcs_df = pd.DataFrame(tcs, columns = tcs.columns) 


# In[41]:


tcs_df.head()


# In[51]:


sn.lineplot(x = "Date",  y ="Close",  data = tcs)


# # Stock Price Going UP over the Years 
# 

# In[ ]:




