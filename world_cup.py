#!/usr/bin/env python
# coding: utf-8

# In[32]:


#Python data analysis library
import pandas as pd

#Python SQL toolkit
from sqlalchemy import create_engine

#PostgreSQL adapter for Python
import psycopg2

frame = pd.read_csv("~/Documents/fifa_match_dataset/World_cup_1930_2022.csv", encoding='Latin1')
engine = create_engine('postgresql://postgres:****@localhost:5432/postgres')

#find duplicates
frame[frame.duplicated(keep='first', subset=None)]


# In[24]:


#remove irrelevant columns
b = frame.drop( columns = [ 'Tournament Id', 'Match Id', 'Group Name', 'Group Stage', 'Knockout Stage', 'Replayed', 'Replay', 'Match Time', 'Stadium Id', 'Stadium Name', 'City Name', 'Home Team Id', 'Away Team Id'], axis=1)
b


# In[25]:


#split the match date 
b[ ["Month", "Day", "Year"]] = b['Match Date'].str.split('/', expand=True)
b


# In[26]:


#remove irrelevant columns:match date, month and day
c = b.drop( columns = ['Match Date', 'Month', 'Day'], axis=1)

c


# In[33]:


c.to_sql('world_cup', con=engine )

