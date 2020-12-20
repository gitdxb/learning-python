#!/usr/bin/env python
# coding: utf-8

# In[3]:


allGuest = {'Alice': {'apples': 5, 'pretzels': 12},
           'Bob': {'ham sandwiches': 3, 'apples': 2},
           'Carol': {'cups': 3, 'apples pies': 1}}
def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought += v.get(item, 0)
    return numBrought
print('Number of things being brought:')
print(' - Apples: ' + str(totalBrought(allGuest, 'apples')))
print(' - Cups: ' + str(totalBrought(allGuest, 'cups')))
print(' - Cakes: ' + str(totalBrought(allGuest, 'cakes')))
print(' - Ham Sandwiches: ' + str(totalBrought(allGuest, 'ham sandwiches')))
print(' - Apple Pies: ' + str(totalBrought(allGuest, 'apples pies')))


# In[8]:


for k,v in allGuest.items():
    print(k,v)


# In[9]:


allGuest.values()


# In[10]:


allGuest.keys()


# In[ ]:




