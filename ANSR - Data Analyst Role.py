#!/usr/bin/env python
# coding: utf-8

# # Question 1

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv(r"C:\Users\Tnluser\Downloads\sales_data.csv")


# In[3]:


df


# In[4]:


df_revenue = df[['product_id','revenue']].groupby('product_id', as_index = False).sum('revenue')


# In[5]:


df_revenue


# In[6]:


plt.bar(x = df_revenue['product_id'],height = df_revenue['revenue'], color = 'blue')
plt.xlabel('Product')
plt.ylabel('Total Revenue')
plt.title('Total Revenue by Product ID')
plt.xticks(df_revenue['product_id'])
plt.show()


# 
# # Question 2

# SELECT empno FROM salaries WHERE salary = (SELECT MAX(salary) FROM salaries);

# # Question 3

# In[7]:


df3=pd.read_csv(r"C:\Users\Tnluser\Downloads\stock_prices.csv")


# In[8]:


df3


# In[9]:


df3['date']=pd.to_datetime(df3['date'], format='%Y-%m-%d')


# In[10]:


df3.head()


# In[11]:


# Calculating rolling 30-day moving average
df3['Rolling_mean'] = df3['closing_price'].rolling(window=30, min_periods=1).mean()
df3


# In[12]:


plt.plot(df3['date'], df3['closing_price'], label='Closing Price')
plt.plot(df3['date'], df3['Rolling_mean'], label='30-Days Rolling Mean', color='green')
plt.xlabel('Date')
plt.ylabel('Price')
plt.xticks(df3['date'], rotation =  90)
plt.title('Closing Price and 30-Days Moving Average')
plt.legend()
plt.grid(True)
plt.show()


# # Question 4

# SELECT activity_date, ROUND(COUNT(DISTINCT CASE WHEN activity_type IS NOT NULL THEN user_id END)*100 /COUNT(DISTINCT user_id),2)
# AS engagement_rate
# FROM
# FROM user_activity
# GROUP BY activity_date
# ORDER BY activity_date;

# # Question 5

# In[13]:


df5=pd.read_csv(r"C:\Users\Tnluser\Downloads\customer_data.csv")


# In[14]:


df5


# In[15]:


df5_cleaned = df5.fillna(0) # replacing NA with 0 here
df5_cleaned.drop_duplicates() # removing duplicates if  any


# In[16]:


df5_cleaned


# In[17]:


df5_avg_purchase_gender = df5_cleaned[['gender','purchases']].groupby('gender').mean()
df5_avg_purchase_gender


# # Question 6

# SELECT product_id, warehouse_id, MAX(date) AS latest_date, SUM(quantity) AS total_quantity
# FROM inventory
# GROUP BY product_id, warehouse_id;
# 

# # Question 7

# In[18]:


df7 = pd.read_csv(r"C:\Users\Tnluser\Downloads\mobile_events_2020.csv")
df7.head()


# In[19]:


# 1. % of sessions with an intention to book a scooter
# get the unique values from event_name
unique_event = df7['event_name'].unique()
print(unique_event)


# In[20]:


df7_unique_id = df7[['anonymous_id', 'event_name','created_at']].groupby(['anonymous_id'], as_index =False).value_counts()
df7_unique_id.head(20) # check a user behaviour


# In[21]:


intention_to_book_scooter = ['Scooter Selected - User', 'Scooter Selected - Auto', 'Location Services Dialogue Opened', 'Location Services Enabled']
intention_percentage=df7['event_name'].isin(intention_to_book_scooter).value_counts()*100/len(df7)
intention_percentage


# In[22]:


# 2. % of sessions with a successful booking
successfull_booking_percent = df7.loc[df7['event_name']=='Ride Started - Successful','event_name'].value_counts()*100/len(df7)
successfull_booking_percent


# # 3.  What determines, according to you, an intention to book?
# When event_name is on fromthe following:
#     'Scooter Selected - User', 'Scooter Selected - Auto', 'Location Services Dialogue Opened', 'Location Services Enabled'
# # 4. What are factors, according to you, determining a successful booking? 
# When the ride has started

# # Question 8

# https://drive.google.com/file/d/1uqK73H9kA-PQCLQUFRUViqSpF4b4sy7A/view?usp=drive_link

# # Question 14

# Data Profiling
# Data Cleansing
# Data Mapping
# Data Validation
# Data Transformation
# Data Versioning
# Data Governance
# Collaboration

# In[ ]:




