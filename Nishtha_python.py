#!/usr/bin/env python
# coding: utf-8

# In[35]:


name = ( "Nishtha Malhotra" )


# In[36]:


email = ( "nishtham17@gmail.com" )


# In[37]:


slack_username = ( "@Nishtha" )


# In[38]:


biostack = ( "genomics/transcriptomics/data science/software development/vaccine informatics" )


# In[39]:


twitter_handle = ( "@nishu_malhotra" )


# In[46]:


def hamming_distance(slack_username, twitter_handle):
    i = 0
    count = 0
    
    while (i < len(slack_username)) :
        if (slack_username[i] != twitter_handle[i]) :
             count += 1
        i += 1 
    return count


# In[47]:


print ( name , email , slack_username , biostack , twitter_handle , hamming_distance(slack_username, twitter_handle), sep = ',' )


# In[ ]:




