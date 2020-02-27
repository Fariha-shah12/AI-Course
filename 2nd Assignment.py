#!/usr/bin/env python
# coding: utf-8

# ## 1. Divisibility Check of two numbers
# 
# Write a Python program to check whether a number is completely divisible by another number. Accept two integer values form the user
# ##### Program Console Sample Output 1:
# Enter numerator: 4
# 
# Enter Denominator: 2
# 
# Number 4 is Completely divisible by 2
# ###### Program Console Sample Output 2:
# Enter numerator: 7
# 
# Enter Denominator: 4
# 
# Number 7 is not Completely divisible by 4

# In[45]:


user_input1= int(input("enter the numerator: "))
user_input2= int(input("enter the denominator: "))
if user_input1%user_input2 ==0:
    print("number ",user_input1,"is divisible by ",user_input2)
    user_input3= int(input("enter the numerator: "))
    user_input4= int(input("enter the denominator: "))
    if user_input3% user_input4 == 0 :
        print("number ",user_input3,"is divisible by ",user_input4)
    else:
        print("number ",user_input3,"is not divisible by ",user_input4)
else :
    print("number ",user_input1,"is not divisible by ",user_input2)


# ###### 2. Copy string n times
# Write a Python program to get a string which is n (non-negative integer) copies of a given string.
# Program Console Output:
# Enter String: Hi
# 
# How many copies of String you need: 4
# 
# 4 Copies of Hi are HiHiHiHi

# In[43]:


n=input()
x=int(input("How many copies of String you need: "))
output = x * n
print( output )


# # 3. Vowel Tester
# Write a Python program to test whether a passed letter is a vowel or not
# #### Program Console Output 1:
# Enter a character: A
# 
# Letter A is Vowel
# #### Program Console Output 2:
# Enter a character: e
# 
# Letter e is Vowel
# #### Program Console Output 2:
# Enter a character: N
# Letter N is not Vowel

# In[44]:


character1= input("enter a character :")
character1=character1.upper()
if character1 == 'A' :
    print(character, "is vowel") 
elif character1 =='E' :
    print(character, "is vowel")
elif character1 == 'I' :
    print(character, "is vowel")
elif character1 == 'O' :
     print(character, "is vowel")
elif character1 == 'U' :
    print(character, "is vowel")
else :
    print(character, "is not vowel")


# ## 4. Odd No.s
# Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number.

# In[19]:


x= int(input("enter the number:"))
for num in range(1,21):
    if num%2 != 0 :
        print(num)


# # 5. Food Slicing
# Make a python program that contains your nine favourite dishes in a list called foods.Print the message, 
# 
# **The first three items in the list are:**
# 
# Then use a slice to print the first three items from that program’s list.Print the message, 
# 
# **Three items from the middle of the list are:**
# 
# Use a slice to print three items from the middle of the list.Print the message, 
# 
# **The last three items in the list are:**
# 
# Use a slice to print the last three items in the list.

# In[36]:


dishes = ['sandwich', 'beef burger', 'fries', 'omelette', 'cheese burger', 'freid rice', 'pasta', 'corn soup', 'veg roll']
slice= dishes[0:3]
slice


# In[37]:


slice = dishes[3:6]
slice


# In[39]:


slice = dishes[6:9]
slice


# In[ ]:




