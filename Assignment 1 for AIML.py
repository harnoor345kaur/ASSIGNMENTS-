#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
csv_1 = pd.read_csv("C:\diamonds.csv", nrows=5)
csv_1


# In[8]:


import pandas as pd
csv_1 = pd.read_csv("C:\diamonds.csv")
print(csv_1["carat"])


# In[6]:


import pandas as pd
csv_1 = pd.read_csv("C:\diamonds.csv")
csv_1 = csv_1.rename(columns={'x':'length', 'y':'width'})
csv_1


# In[2]:


import pandas as pd
csv_1 = pd.read_csv("C:\diamonds.csv")
csv_1.sort_values(
    by="cut",
    ascending=True,
    kind="mergesort"
)


# In[3]:


import pandas as pd
csv_1 = pd.read_csv("C:\diamonds.csv")
result = csv_1[csv_1.cut.isin(['Good', 'Fair', 'Premium'])]
print(result)


# In[7]:


import pandas as pd
csv_1 = pd.read_csv("C:\diamonds.csv")
csv_1


# In[3]:


import pandas as pd
csv_1 = pd.read_csv("C:\diamonds.csv")
result = csv_1.loc[csv_1.cut == 'Good']
print(result.describe())
result = csv_1.loc[csv_1.cut == 'Fair']
print(result.describe())
result = csv_1.loc[csv_1.cut == 'Premium']
print(result.describe())


# In[3]:


import pandas as pd
csv_1 = pd.read_csv("C:\diamonds.csv")
csv_1.cut.value_counts().plot(kind="bar")


# In[4]:


import pandas as pd
csv_1 = pd.read_csv("C:\diamonds.csv")
csv_1.describe()


# In[ ]:




