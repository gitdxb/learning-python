#!/usr/bin/env python
# coding: utf-8

# In[1]:


spam = ['apples', 'bananas', 'tofu', 'cats']


# In[35]:


import sys
def ins(someList):
    try:
        if len(someList) == 0:
            sys.exit()
    except SystemExit:
        print('Your list has no item')
    else:
        someList[-1] = 'and ' + someList[-1]
        newLst = ', '.join(someList)
        print(newLst)

ins(spam)


# In[36]:


zbam = spam = ['apples', 'bananas', 'tofu', 'cats']
ins(zbam)


# In[37]:


lst = ['a', 'b', 'c', 'd', 'e','f']
ins(lst)


# In[38]:


empt = []


# In[39]:


ins(empt)

