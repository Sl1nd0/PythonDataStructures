########################################## 
####  EXERCISE 1 30 MARKS############ 
########################################### 
# 
# Student name:  Silindokuhle Nkabinde
# Student no: 214773872 
# Date:  2024/08/25
# Assignment 3: Python 
# 
# Time to review all the basic data types we learned! This should be a 
# relatively straight-forward and quick assignment. 
################## 
## Problem 1 - 10 Points## 
################## 
# Given the string: 
s= 'fullstackslp' 
# Use indexing to print out the following: 

# 'f' 
print(s[s.index("f")]); 
# 'p' 
print(s[s.index("p")]); 
# 'stack' 
#print from the index of the start character for "stack" in "fullstackslp" up to the 1st character after the word stack in "fullstackslp"
print(s[s.index("stack"):s.index("stack")+len("stack")]); 
# 'slp' 
print(s[s.index("slp"):s.index("slp")+len("slp")]);
# 'cks'  
print(s[s.index("cks"): s.index("cks")+len("cks")])
 
# Bonus: Use indexing to reverse the STRINGS 
print(s[(s.index("fullstackslp")+len("fullstackslp"))::-1]) 

#test = "abc";
#x= lambda test, print(test[1])
 
############## 
## Problem 2 - LISTS - 5 Marks## 
############## 
 
 
# Using keys and indexing, grab 'hello' from the following Dictionaries: 
 
 
d1 = {'simple_key':'hello'} 
print(d1['simple_key']) 
  
d2 = {'k1':{'k2':'hello'}} 
print(d2['k1']['k2']) 
 
 
d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]} 
print(d3['k1'][0]['nest_key'][1][0]) 
 
 
############### 
## Problem 4 - SETS - 4 Marks## 
############### 
 
# USe a set to find the unique values of the list below: 
 
mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3] 
#Your code here: 
 
############### 
## Problem 5 - FORMATTING - 5 Marks## 
############### 
 
 
# You are given the variables:

ge = 45 
name = "Kyle" 
# Use print formatting to print the following string 
# "Hello my dog's name is Kyle and he looks 45 years old" 
print() 