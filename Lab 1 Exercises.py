#!/usr/bin/env python
# coding: utf-8

# In[1]:


def main ():
    if __name__ == "__main__":
        main()


# In[2]:


print ("Hello World");


# In[5]:


# Task 1

name = input("Enter your name: ")
print (name)


# In[1]:


# Task 2

userinput = input("Enter a senctence: ")
userinput = userinput.lower()

print(len(userinput))


# In[3]:


# Task 3

user_height_cm = 0
neighbour1_height_cm = 0
neighbour2_height_cm = 0
avg_height_cm = 0

user_height_cm = int(input("Enter your height in cm: "))
neighbour1_height_cm = int(input("Enter the height of your first neighbour"))
neigbhour2_height_cm = int(input("Enter the height of your second neighbour"))

avg_height_cm = (user_height_cm + neighbour1_height_cm + neighbour2_height_cm) / 3

print ("The average height is ", avg_height_cm)


# In[9]:


# Task 4

user_height_cm = 0
neighbour1_height_cm = 0
neighbour2_height_cm = 0
avg_height_cm = 0
avg_height_inches = 0

user_height_cm = int(input("Enter your height in cm: "))
neighbour1_height_cm = int(input("Enter the height of your first neighbour"))
neigbhour2_height_cm = int(input("Enter the height of your second neighbour"))

avg_height_cm = (user_height_cm + neighbour1_height_cm + neighbour2_height_cm) / 3
print ("The average height in cm is ", avg_height_cm)

avg_height_inches = avg_height_cm / 2.54
print ("The average height in inches is ", avg_height_inches)


# In[15]:


# Task 5

user_height_cm = 0
neighbour1_height_cm = 0
neighbour2_height_cm = 0
avg_height_cm = 0
avg_height_inches = 0

user_height_cm = int(input("Enter your height in cm: "))
neighbour1_height_cm = int(input("Enter the height of your first neighbour in cm: "))
neigbhour2_height_cm = int(input("Enter the height of your second neighbour in cm: "))

avg_height_cm = ((user_height_cm + neighbour1_height_cm) + neighbour2_height_cm)/3
print ("The average height in cm is ", avg_height_cm)

avg_height_inches = avg_height_cm / 2.54
print ("The average height in inches is ", avg_height_inches)

avg_height_feet = avg_height_inches // 12
remaining_inches = avg_height_inches % 12

print ("The average height is ", avg_height_feet, " feet ", remaining_inches, " inches")


# In[17]:


# Task 6

user_height_feet = int(input("Enter your height in feet: "))
user_height_inches = int(input("Enter your height in inches: "))
user_height_total_inches = int((user_height_feet)*12 + (user_height_inches))

neighbour1_height_feet = int(input("Enter the height of your first neighbour in feet: "))
neighbour1_height_inches = int(input("Enter the height of your first neighbour in inches: "))
neighbour1_height_total_inches = int((neighbour1_height_feet)*12 + (neighbour1_height_inches))

neighbour2_height_feet = int(input("Enter the height of your second neighbour in feet: "))
neighbour2_height_inches = int(input("Enter the height of your second neighbour in inches: "))
neighbour2_height_total_inches = int((neighbour2_height_feet)*12 + (neighbour2_height_inches))

avg_height_inches = int((user_height_total_inches + neighbour1_height_total_inches + neighbour2_height_total_inches))

avg_height_feet = int(avg_height_inches)/12
avg_height_remaining_inches = int(avg_height_inches % 12)

print ("The average height is ", avg_height_feet, " feet ", avg_height_remaining_inches, " inches")


# In[ ]:




