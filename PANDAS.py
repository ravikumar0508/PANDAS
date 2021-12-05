#!/usr/bin/env python
# coding: utf-8

# In[9]:



"""#TO accessing the data base 




#to create data base and manipulate also



#to create Data base:-pd.Dataframe




import pandas as pd



#used as a data analytical tool



python Data analytical library





#FEAUTURES OF Pandas
   fast  and efficient
   reshaping and pivoting data
   slice a large data 
   add and deleting data
   time series functionality
   we can use grouping
   
   
TO install in pip and conda
#pip install pandas
#conda install-c anaconda pandas


TO CHECK installation
type import pandas if no error then its well and good


Pandas- series
Series is a one dimensional array like structure with homogeneous
collection of single data types

if its combained more than one data type its called objected series
 it have indexes and data values
 by default start from 0


pandas.series(data,indes,dtype,copy)



CREAATION OF SERIES
 Empty series
 array
 dictionary
 scalar values of constants
 
Empty series
"""
import pandas as pd
pd.Series

#create from numpy arrays
import numpy as np
data =np.array([10,20,30,40,50])
data
   
#creatind Data fro arrays


# In[12]:


#creatind Data fro arrays without indexing
pd.Series(data = data)


# In[13]:


#with index
pd.Series(data=data,index =range(1,6))


# In[14]:


#to change the data type 
pd.Series(data=data,index = range(1,6),dtype ='float')


# In[16]:


#from dicrionary #keys are rows and values are values 


#more than argments theows  NAN
d ={'a':100,'b':200,'c':300}
pd.Series(data=d,index=['a','b','c'])


# In[18]:


#SCALAR VALUES

pd.Series([1,2,3,4,5])


# In[20]:


#DAta Frame 
#empty 

df = pd.DataFrame
df


# In[21]:


#from list create a data frame

data =[1,2,3,4,5,6,7,8]
pd.DataFrame(data)


# In[24]:


data =[1,2,3,4,5,6,7,8]
df = pd.DataFrame(data,columns =['id'])
df


# In[25]:


#from nested list

data =[['ravi',100],['guna',200],['garun',300]]
df = pd.DataFrame(data,columns =['names','age'])
df


# In[27]:


#from Dictionary #keys coloumns and values as per coloumns


data ={'names':['ravi','guna','partha','mathan'],'age':[28,24,29,42]}
df = pd.DataFrame(data,columns =['names','age'])
df


# In[ ]:


#Itreation in pandas


@iteritems-iterate over the (key,value) pairs


@iterrows  -itreate over the rows as (index,series)pairs


@itertuples -itreates over the rows as named tuple


# In[31]:


import pandas as pd
import numpy as np
data =[10,20,30,40,50]
df = pd.Series(data)
df


# In[32]:


#seires iterate

for x in data:
    print(x)


# In[33]:


for x in df:
    print(x)


# In[62]:


d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])
}
columns =['Name','Age','Rating']
df =pd.DataFrame(d)
df


# In[49]:


#Series Basic Functionality

data =np.random.randn(10)
data
df  =pd.Series(data)
df




# In[50]:


#AXES -return index values
df.axes


# In[51]:


#dtype
df.dtype


# In[52]:


#emppty
df.empty


# In[53]:


#ndim
df.ndim


# In[54]:


#size - nof elements

df.size


# In[55]:


#Values -empty array

df.values


# In[61]:


#Head -top values


df.head()
df.head(2)


# In[60]:


#tail -bottom values


df.tail()
df.tail(2)


# In[63]:


#DATA FRAAME BASIC FUNCTIONALITY

d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])
}
df =pd.DataFrame(d)
df
 


# In[64]:


#axes-details about the given data

df.axes


# In[66]:


#dtypes-type of elements


df.dtypes


# In[67]:


#ndim-dimension

df.ndim

#series dimension -1 data frame dimension -2


# In[68]:


#Size-returns size\


df.size


# In[72]:


#head -top elements

df.head(2)


# In[73]:


#tail -low elements

df.tail(2)


# In[74]:


#T-transforce using for matrix and vectoe operations transfers rows into coloumns


df.T



# In[76]:


#Descriptive statsistics

data= {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])
}
df =pd.DataFrame(data)
df


# In[77]:


#count -missing values wont count if its NAN means


df.count()


# In[78]:


#sum -sum everything give everything in a single call

df.sum()


# In[79]:


#mean -Average values return


df.mean()


# In[80]:


#median - return median value

df.median()


# In[81]:


#mode -to find repeating values

df.mode()


# In[82]:


#Standard diviasion 

df.std()


# In[85]:


#min and max

#df.min()
df.max()


# In[89]:


#absolute

df['Age'].abs()


# In[90]:


#prod() -product

df.prod()


# In[91]:


#cumulative sum -df.cumsum() add each and every phreses

df.cumsum()


# In[93]:


#cumlative product -str not working

df['Rating'].cumprod()


# In[94]:


#describe -describe evertything

df.describe()


# In[96]:


#Function PIPE


#uses -apply complete data files at a time

data =np.random.randint(1,6,[4,3])
data


# In[97]:


#supply data frame

df =pd.DataFrame(data =data,columns="col1 col2 col3".split())
df


# In[99]:


#By using functions we can manipulate datas and 



def add_numbers(first,last):
    return first + last
df.pipe(add_numbers,10)


# In[100]:


def subtracrt(first,last):
    return last-first
df.pipe(subtracrt,10)


# In[101]:


def subtracrt(first,last):
    return first-last
df.pipe(subtracrt,10)


# # FUNCTION APPLY METHODS

# In[3]:


import pandas as pd
import numpy as np
data =np.random.randint(1,6,[4,3])
df =pd.DataFrame(data=data,columns="col1 col2 col3".split())
df


# In[4]:


#USER DEFINED FUNCTION

def double_number(num):
    return 2*num
df.apply(double_number)


# In[5]:


df.apply(double_number, axis = 1)


# In[6]:


df.apply(np.sum,axis=1)


# In[7]:


df


# In[8]:


df["col1"].apply(double_number)


# In[10]:


df.loc[2:2:]


# In[11]:


df.loc[2:2:].apply(double_number)


# # APPLY MAPS

# In[12]:


import pandas as pd

import numpy as np

data =np.random.randint(1,6,[4,3])
data


# In[15]:


df =pd.DataFrame(data)
df


# In[16]:


df =pd.DataFrame(data=data,columns ="col1 col2 col3".split())
df


# In[ ]:


counter =0
def double_number(num):
    global cunter
    counter +=1
    return 2*num


# In[19]:


counter =0
df.pipe(double_number)
counter


# In[ ]:




