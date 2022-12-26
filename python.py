#list of common stuff https://datacamp-community-prod.s3.amazonaws.com/0eff0330-e87d-4c34-88d5-73e80cb955f2


#log x axis

# Change the line plot below to a scatter plot
plt.scatter(gdp_cap, life_exp)

# Put the x-axis on a logarithmic scale

plt.xscale('log')

# Show plot
plt.show()



#histograms

# Create histogram of life_exp data



plt.hist(life_exp, bins=10)

# Display histogram
plt.show()





#clean and plot new histogram


# Build histogram with 5 bins

plt.hist(life_exp, bins = 5)
# Show and clean up plot
plt.show()
plt.clf()

# Build histogram with 20 bins

plt.hist(life_exp, bins = 20)

# Show and clean up again
plt.show()
plt.clf()



#add x, y and title

# Basic scatter plot, log scale
plt.scatter(gdp_cap, life_exp)
plt.xscale('log') 

# Strings
xlab = 'GDP per Capita [in USD]'
ylab = 'Life Expectancy [in years]'
title = 'World Development in 2007'

# Add axis labels

plt.xlabel(xlab)
plt.ylabel(ylab)


# Add title

plt.title(title)
# After customizing, display the plot
plt.show()






#using ticks for changing the axis


# Scatter plot
plt.scatter(gdp_cap, life_exp)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')

# Definition of tick_val and tick_lab
tick_val = [1000, 10000, 100000]
tick_lab = ['1k', '10k', '100k']

# Adapt the ticks on the x-axis
plt.xticks(tick_val, tick_lab)

# After customizing, display the plot
plt.show()





#scatter with point size (where the size of the dots correspond to the size of the population)

# Import numpy as np

import numpy as np

# Store pop as a numpy array: np_pop

np_pop = np.array(pop)

# Double np_pop
np_pop = 2*np_pop

# Update: set s argument to np_pop
plt.scatter(gdp_cap, life_exp, s = np_pop)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])

# Display the plot
plt.show()




#getting indexes from a list and printing

# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# Get index of 'germany': ind_ger
ind_ger = countries.index("germany")

# Use ind_ger to print out capital of Germany
print(capitals[ind_ger])



#relation between keys and values


# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Print out the keys in europe
europe.keys()

# Print out value that belongs to key 'norway'
europe['norway']
#remove item from dictionary
del(europe['australia'])



#python indexing iloc (for indexes) and loc (for labels)

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out first 3 observations

print(cars[0:3])

# Print out fourth, fifth and sixth observation
print(cars.iloc[[3,4,5], :])





#Hypothesis tests and z-scores

#The z-score is a standardized measure of the difference between the sample statistic and the hypothesized statistic.


#obs.: Significance level: is beyond a reasonable doubt for hypothesis testing

#either Ha or H0 is true (not both)

#obs.: H0 is initially assumed to be true


#obs.: p-values: probability of obtaining a result, assuming the null hyp. is true.

calculation:

# Calculate the z-score of late_prop_samp
z_score = (late_prop_samp-late_prop_hyp)/std_error

# Calculate the p-value
p_value = 1 - norm.cdf(z_core, loc = 0, scale = 1)
                 
# Print the p-value
print(p_value) 

