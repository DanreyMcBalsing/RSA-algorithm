#!/usr/bin/env python
# coding: utf-8

# In[26]:
from math import gcd
def coprime_2(a,b):
    if(gcd(a,b)==1):
        return True
    else:
        return False
    
#or we can run the code below:    


# from math import gcd
# def coprime(a,b):
#     return gcd(a,b)==1

p=5
q=7
n=p*q
z=(p-1)*(q-1)

for i in range(0,n):#"e" has to be smaller than n
    if(coprime(i,z)==1):
        print(i)

#or we can do it without using any libraries
#for i in range(0,n):
#     if(i%z!=0):
#         print (i)


# In[30]:


#we choose variable "e" the way we want :) and then we compute variable "d"
print("n:",n)
print("z:",z)
e=5
for i in range(0,z):
    if(e*i%z==1):#as we saw on the slides,e*d mod z should be equal to 1
        d=i
        print ("d:",d)#prints "d"


# In[32]:


#now we use variables e and d to do the encryption
#we represent our message in both decimal and binary representation
m=bin(12) #binary representation of our message
decimal_m=12
#c=m**e mod n...so we have :
c=(decimal_m**e)%n
print (c)#prints decimal representation


# In[33]:


#https://beginnersbook.com/2018/02/python-program-to-convert-decimal-to-binary/
def decimalToBinary(num):
    """This function converts decimal number
    to binary and prints it"""
    if num > 1:
        decimalToBinary(num // 2)
    print(num % 2, end='')
decimalToBinary(c)


# In[34]:


#decryption
m=(c**d)%n
print(m)


# In[35]:


decimalToBinary(m)


# In[ ]:




