#!/usr/bin/env python
# coding: utf-8

# In[6]:


unit = input("What is the unit of measurement, Km or miles? ")
type(unit)

distance = input("What is the distance?")
type (distance)

if str.isdigit(distance):
    dig_distance = int(distance)

if unit == "miles":
    
    km_distance = int(dig_distance * 1.609344)
    print("Your distance in Km is ")
    print(km_distance)

elif unit == "Km":
    
    miles_distance = int(dig_distance * 0.621371)
    print("Your distance in miles is ")
    print(miles_distance)
    
else:
    print ("Pick a unit of measurment")


# In[ ]:




