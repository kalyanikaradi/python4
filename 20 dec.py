#!/usr/bin/env python
# coding: utf-8

# In[1]:


#data types 
#list
L1=[2,3,4,5,6,7]
L1


# In[3]:


L2=[3,4.3,6,8,9.1,2,1,7]
L2


# In[4]:


L3=['pune',22.4,6,78]
L3


# In[5]:


list=[2,33,67,99,44,21,56]
list


# In[6]:


list[2:3]


# In[7]:


list[2:6]


# In[8]:


list[1:3:6]


# In[9]:


list[1:-2]


# In[10]:


list[1:6:1]


# In[11]:


list[3]=89


# In[12]:


list


# In[13]:


list[:]


# In[14]:


list[1:]


# In[15]:


list[:6]


# In[ ]:


#methods
#list methods
#replacing multiple values
list=[2,3,4,84,32,11,89,34,65]


# In[ ]:


list[2:4]=[56,90]


# In[16]:


list


# In[17]:


#count method specify the number of repeated values
points=[1,2,34,56,77,77,89,4,77]
x=points.count(77)
print(x)


# In[18]:


#sort method arrange values in ascending order
numbers=[3,1,5,6,21,78,9]
numbers.sort()
print(numbers)


# In[19]:


#reverse method is used to reverse the order of list
numbers=[7,3,4,2,11,56,78,90]
numbers.reverse()
print(numbers)


# In[20]:


#copy the list
numbers=[4,3,2,6]
x=numbers.copy()
print(x)


# In[21]:


x=max(5,4,3)
print(x)


# In[22]:


x=min(4,5,2)
print(x)


# In[ ]:




