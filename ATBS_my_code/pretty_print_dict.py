#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] += 1
pprint.pprint(count)
print()
print(pprint.pformat(count))  # Same thing


# In[ ]:




