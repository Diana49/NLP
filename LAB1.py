#!/usr/bin/env python
# coding: utf-8

# In[2]:


import nltk
nltk.download('all')


# In[3]:


from nltk.book import*


# In[4]:


# import brown corpus 
from nltk.corpus import brown


# In[5]:


brown.categories()


# In[6]:


# list
brown.words(categories='mystery')[:100]


# In[7]:


brown.words(categories= 'science_fiction')[:100]


# In[8]:


#3 import inaugral corpus 
#Has every presidents inaugural address from 1789-20


# In[9]:


from nltk.corpus import inaugural
inaugural.fileids()


# In[10]:


# list
inaugural.words(fileids='1861-Lincoln.txt')[:100]


# In[11]:


inaugural.words(fileids= '2009-Obama.txt')[:100]


# In[12]:


#import webtextcorpus


# In[13]:


from nltk.corpus import webtext
webtext.fileids()


# In[14]:


for fileid in webtext.fileids(): 
    print(fileid,webtext.raw(fileid)[:])


# In[15]:


text='The term text analytics also describes that application of text analytics to respond to business problems, whether independently or in conjunction with query and analysis of fielded, numerical data. It is a truism that 80 percent of business-relevant information originates'
fd=nltk.FreqDist(text.split()) 
fd


# In[16]:


#conditional frequency distribution 
from nltk.probability import ConditionalFreqDist
c=ConditionalFreqDist((len(word),word) for word in text.split())
#conditons
c.conditions()


# In[17]:


c[5]


# In[ ]:




