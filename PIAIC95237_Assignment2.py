#!/usr/bin/env python
# coding: utf-8

# # Question:1
# #Convert a 1D array to a 2D array with 2 rows?

# In[8]:


import numpy as np
x = np.array([0,1,2,3,4,5,6,7,8,9])
x


# In[10]:


x.reshape(2,5)


# # Question:2
# #How to stack two arrays vertically?

# In[12]:


y = np.ones(10)
y


# In[15]:


arr_x = x.reshape(2,5)
arr_y = y.reshape(2,5)
np.vstack((arr_x,arr_y))


# # Question:3
# #How to stack two arrays horizontally?

# In[16]:


np.hstack((arr_x,arr_y))


# # Question:4
# #How to convert an array of arrays into a flat 1d array?

# In[18]:


array_flat = np.ravel(arr_x)
array_flat


# # Question:5
# #How to Convert higher dimension into one dimension?

# In[19]:


arr2 = np.array([[ 0, 1, 2], [ 3, 4, 5], [ 6, 7, 8], [ 9, 10, 11], [12, 13, 14]])
np.concatenate(arr2)


# # Question:6
# #Convert one dimension to higher dimension?

# In[20]:


arr3 = np.array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14])
np.split(arr3,[3,6,9,12])


# # Question:7
# #Create 5x5 an array and find the square of an array?

# In[23]:


arr4 = np.random.rand(5,5)
arr4


# In[24]:


np.sqrt(arr4)


# # Question:8
# #Create 5x6 an array and find the mean?

# In[25]:


arr5 = np.random.rand(5,6)
arr5


# In[26]:


mean_arr5 = np.mean(arr5)
mean_arr5


# # Question:9
# #Find the standard deviation of the previous array in Q8?

# In[28]:


stddev_arr5 = np.std(arr5)
stddev_arr5


# # Question:10
# #Find the median of the previous array in Q8?

# In[30]:


median_arr5 = np.median(arr5)
median_arr5


# # Question:11
# #Find the transpose of the previous array in Q8?

# In[31]:


trans_arr5 = np.transpose(arr5)
trans_arr5


# # Question:12
# #Create a 4x4 an array and find the sum of diagonal elements?

# In[33]:


arr6 = np.random.rand(4,4)
arr6


# In[34]:


diag_arr6 = np.diag(arr6)
diag_arr6


# In[35]:


np.sum(diag_arr6)


# # Question:13
# #Find the determinant of the previous array in Q12?

# In[38]:


np.linalg.det(arr6)


# # Question:14
# #Find the 5th and 95th percentile of an array?

# In[39]:


arr7 = np.arange(10)
print(arr7)
print(np.percentile(arr7,5))
print(np.percentile(arr7,95))


# # Question:15
# #How to find if a given array has any null values?

# In[43]:


null_val = np.isnan(arr7)
null_val


# In[ ]:




