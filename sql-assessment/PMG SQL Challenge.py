#!/usr/bin/env python
# coding: utf-8

# In[9]:


get_ipython().run_line_magic('load_ext', 'sql')


# In[11]:


get_ipython().run_line_magic('sql', 'sqlite:///OPIM608_CDB.db')
from sqlalchemy import create_engine
import pandas as pd


# In[19]:


marketing_performance=pd.read_csv("marketing_performance.csv")


# In[21]:


website_revenue=pd.read_csv("website_revenue.csv")


# In[22]:


campaign_info=pd.read_csv("campaign_info.csv")


# In[23]:


marketing_performance.head()


# In[24]:


website_revenue.head()


# In[25]:


campaign_info.head()


# In[26]:


engine=create_engine('sqlite:///OPIM608_CDB.db')


# In[27]:


marketing_performance.to_sql('Marketing', engine, if_exists='append',
           index=False)


# In[28]:


campaign_info.to_sql('Campaign', engine, if_exists='append',
           index=False)


# In[29]:


website_revenue.to_sql('Website', engine, if_exists='append',
           index=False)


# ***

# In[32]:


get_ipython().run_cell_magic('sql', '', '/* Query 1*/\n\nSELECT date, SUM(impressions) AS total_impressions\nFROM Marketing\nGROUP BY date\nORDER BY date;')


# ***

# In[36]:


get_ipython().run_cell_magic('sql', '', '/* Query 2*/\n\nSELECT state, SUM(revenue) AS total_revenue\nFROM Website\nGROUP BY state\nORDER BY total_revenue DESC\nLIMIT 3;')


# The third best performing state by revenue was Ohio with a total revenue of $37,577.

# ***

# In[37]:


get_ipython().run_cell_magic('sql', '', '/* Query 3*/\n\nSELECT c.name AS campaign_name, \n       SUM(mp.cost) AS total_cost,\n       SUM(mp.impressions) AS total_impressions,\n       SUM(mp.clicks) AS total_clicks,\n       SUM(wr.revenue) AS total_revenue\nFROM  Campaign c\nJOIN Marketing mp ON c.id = mp.campaign_id\nJOIN Website wr ON c.id = wr.campaign_id\nGROUP BY c.name;')


# ***

# In[73]:


get_ipython().run_cell_magic('sql', '', '/* Query 4*/\n\nSELECT c.name AS campaign_name, wr.state,\nSUM(mp.conversions) AS total_conversions\nFROM  Campaign c\nJOIN Marketing mp ON c.id = mp.campaign_id\nJOIN Website wr ON c.id = wr.campaign_id\nWHERE c.name = "Campaign5"\nGROUP BY wr.state\nORDER BY total_conversions DESC\nLIMIT 1;')


# Georgia performed the most conversions in Campaign 5.

# ***

# In[40]:


get_ipython().run_cell_magic('sql', '', '/* Query 5*/\nSELECT c.name AS campaign_name,\n       SUM(mp.cost) / SUM(mp.conversions) AS cost_per_conversion\nFROM Campaign c\nJOIN Marketing mp ON c.id = mp.campaign_id\nGROUP BY c.name\nORDER BY cost_per_conversion ASC\nLIMIT 1;')


# Assuming efficiency is measured by cost per conversion, Campaign 4 was the cheapest cost per conversion campaign.

# ***

# In[77]:


get_ipython().run_cell_magic('sql', '', "/* Bonus Query*/\n\n\nSELECT DATENAME(day, '2017/08/25 08:36') AS day_of_week;\n       AVG(impressions) AS avg_impressions\nFROM Marketing\nGROUP BY day_of_week\nORDER BY avg_impressions DESC\nLIMIT 1;")


# ***
