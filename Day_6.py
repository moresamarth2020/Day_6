#!/usr/bin/env python
# coding: utf-8

# # What are strings?
# In python, anything that you enclose between single or double quotation marks is considered a string. A string is essentially a sequence or array of textual data. Strings are used when working with Unicode characters.

# In[1]:


name = "Harry"
print("Hello, " + name)


# In[9]:


Name = "Samarth" #String in Single Quotation
Frind = 'Ram' #String in Double Quotation
Anotherfrind = 'Sham'
print(Name, Frind, Anotherfrind)


# * It does not matter whether you enclose your strings in single or double quotes, the output remains the same.
# * Sometimes, the user might need to put quotation marks in between the strings. Example, consider the sentence: He said, “I want to eat an apple”.
# * How will you print this statement in python?: He said, "I want to eat an apple". We will definitely use single quotes for our convenience.

# In[26]:


print('He said,"I Want to eat apple"')
#or
print("He said,\"I want to eat apple")


# ## Multiline Strings
# If our string has multiple lines, we can create them like this:

# In[30]:


#Using triple double quotes
a = """Johny Johny, yes papa? 
Eating sugar? No papa
Telling lies? No papa
Open your mouth
Ha, ha, ha
Johny Johny, yes papa?
Eating sugar? No papa
Telling lies? No papa
Open your mouth
Ha, ha, ha
Johny Johny, yes papa?
Johny Johny, yes papa?
Johny Johny, yes papa?
Johny Johny, yes papa?
Johny Johny, yes papa?
Eating sugar? No papa
Telling lies? No papa
Open your mouth
Ha, ha, ha"""

print(a)


# In[31]:


#Using triple single quotes
b = '''Johny Johny, yes papa?
Eating sugar? No papa
Telling lies? No papa
Open your mouth
Ha, ha, ha
Johny Johny, yes papa?
Eating sugar? No papa
Telling lies? No papa
Open your mouth
Ha, ha, ha
Johny Johny, yes papa?
Johny Johny, yes papa?
Johny Johny, yes papa?
Johny Johny, yes papa?
Johny Johny, yes papa?
Eating sugar? No papa
Telling lies? No papa
Open your mouth
Ha, ha, ha'''

print(b)


# ### Accessing Characters of a String
# In Python, string is like an array of characters. We can access parts of string by using its index which starts from 0.
# Square brackets can be used to access elements of the string.

# In[44]:


# Example
string = "Samarth"
print(string[0])
print(string[1])
print(string[2])
print(string[3])
print(string[4])
print(string[5])
print(string[6])


# In[ ]:




