#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Justifying text with rjust(), ljust(), center()
# ATBS's code
def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PINIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
print()
printPicnic(picnicItems, 20, 6)


# In[3]:


'Hello'.rjust(20, '.')


# In[4]:


'Hello'.center(20, '=')


# In[5]:


'Hello'.ljust(20, '*')


# In[ ]:




