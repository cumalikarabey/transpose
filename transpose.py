#!/usr/bin/env python
# coding: utf-8

# # Input  Number of the Matrix

# In[47]:


import numpy  as np

row = int(input("Row dimension: "))
col = int(input("Col dimension: "))

count_1 = 1
count = 1

universe = []

while count_1 < row+1:
    empty = []
    
    while count < col+1:
        x = int(input(f"{count_1}. row {count}. number: "))
        empty.append(x)
        count += 1
        
        
    universe.append(empty)
    count_1 += 1
    count = 1


# # Tranpose Operation

# In[51]:


row = row - 1
count_c = col
t_uni = []

for i in range(count_c):
    count = row
    empty = []
    
    while count != -1:
        x = universe[count][i]
        empty.append(x)
        count -= 1
    
    t_uni.append(empty)
    


# In[50]:


universe, t_uni

