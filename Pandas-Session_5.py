#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[ ]:


df1=pd.DataFrame({'key' :['b', 'a', 'd', 'e'], 'data1' :[0,4,6,8]})  # has unique
df2=pd.DataFrame({'key' :['a', 'b', 'd', 'f'],'data2' :[3,6,9,11]}) # has unique row labels
print("DataFrame1 :\n", df1, '\n DataFrame2 :\n',df2)
print("Inner Join :\n", pd.merge(df1,df2,on='key', how='inner', sort=True))  # intersection of keys


# In[2]:


df_stud = pd.DataFrame({'st_id' : [101,102,103,104,105], 'Branch' : ['IT', 'CS','ECE', 'CS', 'MECH']})
df_fac = pd.DataFrame({'F_id' : [110,120,130,140,150], 'Branch' : ['ECE', 'MECH','EEE', 'IT', 'CS']})
print("Student DataFrame: \n", df_stud, '\n Faculty DataFrame : \n', df_fac)
df_merge=pd.merge(df_stud,df_fac,on='Branch', how='inner', sort=True)
print("Merged DataFrame : \n", df_merge)   #Merge on a column


# In[5]:


df_stud = pd.DataFrame({'st_id' : [101,102,103,104,105], 'Branch' : ['IT', 'CS','ECE', 'CS', 'MECH']})
df_fac = pd.DataFrame({'F_name' : ['A', 'B', 'C', 'D', 'E'], 'Stream' : ['ECE', 'MECH','EEE', 'IT', 'CS']})
print("Student Details: \n", df_stud, '\n Faculty Details : \n', df_fac)
#df_merge=pd.merge(df_stud,df_fac,on='Branch', how='inner', sort=True)
print("Merged DataFrame : \n", pd.merge(df_stud,df_fac,left_on = 'Branch', right_on = 'Stream'))   #Merge on a column


# In[8]:


# The redundant column also dropped
pd.merge(df_stud,df_fac,left_on='Branch',right_on='Stream').drop('Stream',axis=1)


# In[62]:


# The redundant column can also be dropped
new_df=pd.merge(df_stud,df_fac,left_on = 'Branch', right_on='Stream')
new_df
new_df.drop('Stream', axis=1)


# In[9]:


df1=pd.DataFrame({'key' :['b', 'a', 'd', 'e'], 'data1' :[0,4,6,8]})  # has unique
df2=pd.DataFrame({'key' :['a', 'b', 'd', 'f'],'data2' :[3,6,9,11]}) # has unique row labels
print("DataFrame1 :\n", df1, '\n DataFrame2 :\n',df2)


# In[12]:


df1=pd.DataFrame({'key' :['b', 'a', 'd', 'e'], 'data1' :[0,4,6,8]})  # has unique
df2=pd.DataFrame({'key' :['a', 'b', 'd', 'f'],'data2' :[3,6,9,11]}) # has unique row labels
print("DataFrame1 :\n", df1, '\n DataFrame2 :\n',df2)
print("Outer Join :\n", pd.merge(df1,df2, how='outer', left_index=True, right_index=True))  # union of keys


# In[14]:


df1=pd.DataFrame({'key' :['b', 'a', 'd', 'e'], 'data1' :[0,4,6,8]})  # has unique
df2=pd.DataFrame({'key' :['a', 'b', 'd', 'f'],'data2' :[3,6,9,11]}) # has unique row labels
print("DataFrame1 :\n", df1, '\n DataFrame2 :\n',df2)
print("Outer Join :\n", pd.merge(df1,df2, how='outer', left_index=True, right_index=True))  # union of keys
# by default it adds suffixes _x and _yon the same column
# by default how = inner, here we can have all options


# In[19]:


print('\n Using merge on indices: \n', pd.merge(df1,df2,how='outer', left_index=True, right_index=True))


# In[22]:


#DataFrame has a convinient join method for merging by index
#print('\n Using join() : \n', df1.join(df2))
print('\n Using join() : \n',df1.join(df2,lsuffix='_x', rsuffix='_y'))
#lsuffix='_x', rsuffix='_y'
#default is left join


# In[56]:


print("Concatenated DataFrames axis = 1 \n", pd.concat([df1,df2], axis=1))


# In[54]:


print("Concatenated DataFrames axis =0 \n", pd.concat([df1,df2], axis=0))


# In[24]:


#print('\n Using join() : \n', df1.join(df2))
print('\n Using join() : \n',df1.join(df2,lsuffix='_df1', rsuffix='_df2'))
#lsuffix='_x', rsuffix='_y'
#default is left join


# In[30]:


df1=pd.DataFrame({'key' :['b', 'a', 'd', 'e'], 'data1' :[0,4,6,8]}, index=[10,20,30,40])
df2=pd.DataFrame({'key' :['a', 'b', 'd', 'f'], 'data1' :[3,6,9,11]}, index=[40,50,60,70])
print("DataFrame1 :\n", df1, '\n DataFrame2 :\n',df2)
#print('\n', pd.merge(df1,df2,how='inner', left_index=True,right_index=True))
print('\n Using merge on indices:\n', pd.merge(df1,df2,how='inner', left_index=True,right_index=True))


# In[32]:


df1=pd.DataFrame({'key' :['b', 'a', 'd', 'e'], 'data1' :[0,4,6,8]}, index=[10,20,30,40])
df2=pd.DataFrame({'key' :['a', 'b', 'd', 'f'], 'data1' :[3,6,9,11]}, index=[40,50,60,70])
print("DataFrame1 :\n", df1, '\n DataFrame2 :\n',df2)
print('\n', pd.merge(df1,df2,how='inner', left_index=True,right_index=True))
print('\n Using merge on indices:\n', pd.merge(df1,df2,how='inner', left_index=True,right_index=True))


# In[43]:


# If we want to join using the key columns,we need to set key to be index in both df1 and df2
# The joint DataFrame will then have the key as it's index
df1=pd.DataFrame({'key':['b','b','a','c','a'], 'data11':[10,20,30,40,50]})
# has multiple rows lebelled a and b
df2=pd.DataFrame({'key':['a','b','a','d'], 'data12':[100,200,300,400]})
print("DataFrame1 :\n", df1, '\n DataFrame2 :\n',df2)


# In[57]:


dfn1=df1.set_index('key')
dfn2=df2.set_index('key')
print('\n Using merge on indices : \n' , pd.merge(dfn1, dfn2, how='inner', left_index=True, right_index=True))


# In[60]:


dfn1=df1.set_index('key')
dfn2=df2.set_index('key')
print('\n Using merge on indices : \n' , pd.merge(dfn1, dfn2, left_index=True, right_index=True))
#  For merge how=inner
print('\n Using join() : \n', dfn1.join(dfn2,lsuffix='_x', rsuffix='_y'))
# for join how='left' by default


# In[50]:


df1=pd.DataFrame({'key':['b','b','a','c','a'], 'data11':[10,20,30,40,50]})
df2=pd.DataFrame({'key':['a','b','a','d'], 'data12':[100,200,300,400]})
print("DataFrame1 :\n", df1, '\n DataFrame2 :\n',df2)
dfn1=df1.set_index('key')
dfn2=df2.set_index('key')
print(dfn1)
print(dfn2)


# In[51]:


df1=pd.DataFrame({'key':['b','b','a','c','a'], 'data11':[10,20,30,40,50]})
df2=pd.DataFrame({'key':['a','b','a','d'], 'data12':[100,200,300,400]})
print("DataFrame1 :\n", df1, '\n DataFrame2 :\n',df2)
dfn1=df1.set_index('key')
dfn2=df2.set_index('key')
print(dfn1)
print(dfn2)
print('\n Using merge on indices:\n',pd.merge(dfn1,dfn2,left_index=True,right_index=True))


# In[ ]:





# In[ ]:




