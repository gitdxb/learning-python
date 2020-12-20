#!/usr/bin/env python
# coding: utf-8

# In[2]:


spam = {'color': 'red', 'age': 42}
for v in spam.values():
    print(v)


# In[3]:


for k in spam.keys():
    print(k)


# In[4]:


for i in spam.items():
    print(i)


# In[6]:


for k,v in spam.items():
    print(k, v)


# In[7]:


spam.keys()


# In[8]:


list(spam.keys())


# In[10]:


list(spam.keys())[0]


# In[11]:


'color' in spam.keys()


# In[12]:


picnicItems = {'apples': 5, 'cups': 2}
'I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.'


# In[13]:


'I am bringing ' + str(picnicItems.get('chair', 0)) + ' chairs.'


# In[14]:


spam = {'name': 'Pooka', 'age': '5'}
spam.setdefault('color', 'black')


# In[15]:


spam


# In[16]:


spam.setdefault('color', 'white')


# In[17]:


spam


# In[18]:


spam["color"] = 'white'


# In[19]:


spam


# In[25]:


message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character.lower(), 0)
    count[character.lower()] = count[character.lower()] + 1
print(count)


# In[ ]:




