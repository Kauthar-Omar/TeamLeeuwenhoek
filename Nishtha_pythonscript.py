#!/usr/bin/env python
# coding: utf-8

# In[1]:


name = ( "Nishtha Malhotra" )


# In[2]:


email = ( "nishtham17@gmail.com" )


# In[3]:


slack_username = ( "@Nishtha" )


# In[4]:


biostack = ( "genomics/transcriptomics/data science/software development/vaccine informatics" )


# In[5]:


twitter_handle = ( "@nishu_malhotra" )


# In[18]:


s1 = 'slack_username'
s2 = 'twitter_handle'


# In[19]:


def hamming_distance(s1, s2):
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))


# In[20]:


print ( name , email , slack_username , biostack , twitter_handle , hamming_distance(s1, s2), sep = ',' )

