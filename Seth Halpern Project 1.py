
# coding: utf-8

# # Project 1
# 
# ## Step 1: Open the `sat_scores.csv` file. Investigate the data, and answer the questions below.
# 

# ##### 1. What does the data describe?

# The data describe state level SAT participation rates (as a % of eligible students), as well as the average math and verbal scores in each state. The last row is the national participation rate, and average math and verbal scores.

# ##### 2. Does the data look complete? Are there any obvious issues with the observations?

# The data appears to contain all 50 states plus the District of Columbia. While I cannot comment on the accuracy of the data for each state, I am happy to see my homestate of CT right at the top for participation rate (go Nutmeggers!)
# 
# Returning to the question at hand, there is one *potential* issue with the observations. The "All" row average for participation and verbal/math scores differs from the average of the state data listed above in the file. I am hoping that this is because the "All" row is a true national average rather than a distorted average that would result from reliance on state-level data. This is likely the case - and if it is indeed a true national average - I do not see any issues with the observations. 

# ##### 3. Create a data dictionary for the dataset.

# In[95]:

import pandas as pd # import pandas, call it pd
import numpy as np
import csv
sat_scores = pd.read_csv('sat_scores.csv') # read in the data, where the data is a csv

df = []
for index, row in sat_scores.iterrows():
    values = []
    for i, item in enumerate(row):
        values.append(item)   
        #sat_scores[headers[i]] =  item
        df.append(values)
        


#with open('sat_scores.csv', mode='r') as infile: #commenting out the csv module approach in favor of pandas above
#    reader = csv.reader(infile)
#    #next(reader, None) #skip the header row
#    with open ('sat_score.csv', mode='w') as outfile:
#        sat_scores = csv.writer(outfile)


# ## Step 2: Load the data.

# ##### 4. Load the data into a list of lists

# In[96]:

temps = pd.DataFrame(df).drop_duplicates() #rows were repeating four times so had to dedupe



# ##### 5. Print the data

# In[97]:

print temps


# In[56]:

##### 6. Extract a list of the labels from the data, and remove them from the data.
#Performed using pandas, iterrows, and enumerate above


# ##### 7. Create a list of State names extracted from the data. (Hint: use the list of labels to index on the State column)

# In[98]:

temps[0] #slicing dataframe based on column 0


# ##### 8. Print the types of each column

# In[101]:

temps.info()


# ##### 9. Do any types need to be reassigned? If so, go ahead and do it.

# In[ ]:

#I do not believe the types need to be reassigned


# ##### 10. Create a dictionary for each column mapping the State to its respective value for that column. 

# In[ ]:

# Need help


# ##### 11. Create a dictionary with the values for each of the numeric columns

# In[ ]:

# Need help


# ## Step 3: Describe the data

# ##### 12. Print the min and max of each column

# In[112]:

#this appears to be operating on the alphabetical column 0 (state). NEED HELP.
def minMax(temps):
    return pd.Series(index=['min','max'],data=[temps.min(),temps.max()])

temps.apply(minMax)


# ##### 13. Write a function using only list comprehensions, no loops, to compute Standard Deviation. Print the Standard Deviation of each numeric column.

# In[119]:

import math

#getting a "len" error. also need to figure out how to pass in right columns.

def standardDev(temps):
    n = len(2) 
    mean = sum(2) / n 
    dev = [x - mean for x in temps] 
    dev2 = [x*x for x in dev] 
    SD = math.sqrt( sum(dev2) / n) # for the standard deviation of the population 
    
standardDev(temps)


# ## Step 4: Visualize the data

# ##### 14. Using MatPlotLib and PyPlot, plot the distribution of the Rate using histograms.

# In[128]:

import matplotlib
import matplotlib.pyplot as plt 

plt.hist(temps.index)
plt.show()


# ##### 15. Plot the Math distribution

# In[ ]:

# Need help


# ##### 16. Plot the Verbal distribution

# In[ ]:

# Need help


# ##### 17. What is the typical assumption for data distribution?

# In[ ]:

Standard normal distribution with ~68% of all results +- 1 standard deviation, 95% +-2 standard deviations, 99.7% +- 3 standard deviations


# ##### 18. Does that distribution hold true for our data?

# In[ ]:

#Need help


# ##### 19. Plot some scatterplots. **BONUS**: Use a PyPlot `figure` to present multiple plots at once.

# In[ ]:

# :/


# ##### 20. Are there any interesting relationships to note?

# In[ ]:

# ;/


# ##### 21. Create box plots for each variable. 

# In[ ]:

# :/


# ##### BONUS: Using Tableau, create a heat map for each variable using a map of the US. 

# In[ ]:



