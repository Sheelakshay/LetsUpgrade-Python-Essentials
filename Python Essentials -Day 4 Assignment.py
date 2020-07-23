#!/usr/bin/env python
# coding: utf-8

# 1:Find all occurence of substring in the given string,print the index values

# In[15]:


import re
str1="What we think we become;we are python programmer"


# In[19]:


str1.count("we",0,30)
print(str1.find("we"))
[we.start() for we in re.finditer('we', 'What we think we become;we are python programmer')] 


# 2:Explain using islower(),isupper() with different kinds of strings
# 
# Python string method islower() checks whether all the case-based characters (letters) of the string are lowercase.
# 
# The isupper() method returns True if all the characters are in upper case, otherwise False.
# 
# Numbers, symbols and spaces are not checked, only alphabet characters.

# In[5]:


a=input("Enter the string:")
b=a.islower()
c=a.isupper()
print(b)
print(c)


# 

# In[ ]:




