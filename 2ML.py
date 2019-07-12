
# coding: utf-8

# In[2]:


import numpy as np
TwoD = np.array([[2,3,8],[3,4,6],[2,4,6]])
print(TwoD)
print(TwoD[0][0])
print(TwoD[2][1])
print(TwoD[2,2])

print(TwoD[:2])
print(TwoD[:2,0:1])


# In[3]:


new = np.arange(0,10)
slice_of_array=new[0:6]
print(slice_of_array)

slice_of_array[:]=99
print(slice_of_array)

new2 = new.copy()
print(new2)


# In[5]:


lohit=np.arange(1,11)
lohit

bool_arr=lohit>4
bool_arr


# In[10]:


lohit[bool_arr]


# In[11]:


arr = np.arange(25)
ranarr=np.random.randint(0,50,10)
ranarr
arr


# In[12]:


arr[arr<5]


# In[13]:


from numpy.random import randint


# In[14]:


randint(3,22)


# In[15]:


arr_2d=np.arange(40).reshape(4,10)
arr_2d


# In[16]:


import numpy as np
new_array = np.arange(0,11)
new_array


# In[17]:


new_array+new_array


# In[18]:


new_array-new_array


# In[19]:


new_array*new_array


# In[20]:


new_array/new_array


# In[21]:


new=new_array+1000
new


# In[22]:


new = new_array*10
new


# In[23]:


new=new/12
new


# In[25]:


new_array=np.arange(1,10)
new=new_array+new_array
new
n=new/10
n


# In[26]:


ok=np.arange(3,10)
ok


# In[27]:


np.sqrt(ok)


# In[28]:


np.max(ok)


# In[29]:


np.min(ok)


# In[30]:


np.sin(ok)


# In[32]:


np.log(ok)


# In[34]:


log_number=np.arange(0,3)
print(np.log(log_number))


# In[96]:


n=np.zeros(10)
n


# In[105]:


n+5


# In[106]:


np.ones(10)*5


# In[112]:


N= (np.arange(100).reshape(10,10)+1)/100
N


# In[113]:


np.arange(1,101).reshape(10,10)/100


# In[100]:


np.linspace(0,1,20)


# In[42]:


np.arange(10,51)


# In[108]:


np.arange(9).reshape(3,3)


# In[109]:


np.eye(3)


# In[110]:


np.random.rand()


# In[111]:


np.linspace(0,50,200)


# In[46]:


np.random.randn(25)


# In[107]:


np.arange(10,51,2)


# In[114]:


n = np.arange(25).reshape(5,5)+1
n


# In[117]:


n = np.arange(1,26).reshape(5,5)
n


# In[118]:


print(n[2:,1:])


# In[77]:


np.sum(n)


# In[80]:


print(n[4:5])


# In[78]:


print(n[3:5])


# In[116]:





# In[62]:


np.array([[12,13,14,15],[17,18,19,20],[22,23,24,25]])


# In[85]:


np.array(n[0:3,1:2])


# In[104]:


np.sqrt(52)


# In[103]:


np.arange(11,16)*5

