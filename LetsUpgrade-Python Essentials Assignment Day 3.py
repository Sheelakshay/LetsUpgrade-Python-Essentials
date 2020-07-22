#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Question 1: To find the sum of n numbers  using while loop
n = int(input("enter the number "))

# To initialize the sum and counter
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i+1    # update the counter

# print the sum
print("The sum is", sum)


# In[3]:


# Question 2:To check if number is prime or not
num = int(input("Enter a number: "))  
  
if num > 1:  
   for i in range(2,num):  
       if (num % i) == 0:  
           print(num,"is not a prime number")  
           print(i,"times",num//i,"is",num)  
           break  
   else:  
       print(num,"is a prime number")  
         
else:  
   print(num,"is not a prime number")





# In[ ]:




