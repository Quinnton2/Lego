#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/KeithGalli/lego-analysis/master/datasets/lego_sets.csv')
theme = pd.read_csv('https://raw.githubusercontent.com/KeithGalli/lego-analysis/master/datasets/parent_themes.csv')


# In[4]:


theme.head()


# In[11]:


df.head(50)


# In[9]:


import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/KeithGalli/lego-analysis/master/datasets/lego_sets.csv')
theme = pd.read_csv('https://raw.githubusercontent.com/KeithGalli/lego-analysis/master/datasets/parent_themes.csv')


# In[10]:





# In[29]:


merged = df.merge(theme, left_on= 'parent_theme', right_on='name')
merged.head()


# In[30]:


merged = df.merge(theme, left_on= 'parent_theme', right_on='name')
merged.drop(columns='name_y', inplace=True)
merged.head()


# In[36]:


licensed = merged[merged['is_licensed']]
licensed.head()

star_wars = licensed[licensed['parent_theme']=='Star Wars']

star_wars.head(50)


# In[45]:


merged[merged['set_num'].isnull()].shape


# In[46]:


licensed = merged[merged['is_licensed']]
licensed = licensed.dropna(subset=['set_num'])
licensed.head()

star_wars = licensed[licensed['parent_theme']=='Star Wars']

the_force = int(star_wars.shape[0]/licensed.shape[0]*100)
print(the_force)


# In[47]:


licensed.head()


# In[51]:


licensed_sorted = licensed.sort_values('year')
licensed_sorted['counted'] = 1
licensed_sorted.head()

#licensed_sorted.groupby(['year','parent_theme']).


# In[53]:


licensed_sorted = licensed.sort_values('year')
licensed_sorted['counted'] = 1

summed_df = licensed_sorted.groupby(['year','parent_theme']).sum().reset_index()

summed_df.head()


# In[59]:


licensed_sorted = licensed.sort_values('year')
licensed_sorted['counted'] = 1

summed_df = licensed_sorted.groupby(['year','parent_theme']).sum().reset_index()

summed_df.head()


# In[61]:


licensed_sorted = licensed.sort_values('year')
licensed_sorted['counted'] = 1

max_df = licensed_sorted.groupby(['year','parent_theme']).sum().reset_index()

max_df.sort_values('year', inplace=True)
max_df


# In[62]:


new_era = 2017 


# In[ ]:




