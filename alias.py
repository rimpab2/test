#!/usr/bin/env python
# coding: utf-8

# In[11]:


import os

os.system('alias cdd="cd ~/Desktop/"')


# In[12]:


#this code just to show the making alias
a = 5
b = a
print id(a), id(b)
 
c = b
b = 3
print a,b,c
print id(a),id(b),id(c)
 
b = a
b = 5
print id(a), id(b)


# In[ ]:




