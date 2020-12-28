#!/usr/bin/env python
# coding: utf-8

# In[6]:


#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard - by ATBS

import pyperclip
text= pyperclip.paste()

# Separate lines and add stars
lines = text.split('\n')
for i in range(len(lines)):  # loop through all indexs for "lines" list
    lines[i] = '* ' + lines[i] # add start to each string in "lines" list
    # print(lines[i])
text = '\n'.join(lines)
pyperclip.copy(text)

