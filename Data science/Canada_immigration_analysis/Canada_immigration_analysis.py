#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib as mpl

# skip the first 20 rows and the last 2 rows because they are just text not tabulated data
df = pd.read_excel('https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DV0101EN/labs/Data_Files/Canada''.xlsx',
sheet_name='Canada by Citizenship',
skiprows=range(20),
skipfooter=2)
print(df.head())
print(df.columns)

# get rid of some columns that we are not using to make the dataset smaller and manageable
df.drop(['AREA','REG', 'DEV', 'Type', 'Coverage'], axis=1, inplace=True)
print(df.head())
print(df.columns)

# Change the column names to something more understandable
df.rename(columns={"OdName": "Country", "AreaName": "Continent" , "RegName": "Region"}, inplace=True)
print(df.head())
print(df.columns)


#use to get each column index
print(df.columns.get_loc(2013))

#iloc give the columns range to get the sum of immigrants for all the years for each country
#add a 'total' column which will show the total immigrants that came into Canada from 1980 to 2013 from each country
df['Total']=df.iloc[:,4:38].sum(axis=1)
print(df.head())

# Check if there are any null values in any of the columns
print(df.isnull().sum())

# Set the 'Country" column as the index
df = df.set_index("Country")
print(df.head())

print(df)

# starting plot data 
# check for the availale plot styles and here we use 'ggplot'
print(plt.style.available)
mpl.style.use(["ggplot"])

# immigration data of Switzerland and the years to a line grapgh.
years = list(map(int, range (1980, 2014)))
print(years)

print(df.loc["Switzerland",years])

df.loc["Switzerland",years].plot()
plt.title('Immigration from Switzerland') 
plt.ylabel('Number of immigrants') 
plt.xlabel ('Years') 
plt.show()

# immigration data if India, Pakistan and Bangladesh for the years to a line grapgh.
ind_pak_ban = df.loc[['India', 'Pakistan','Bangladesh'], years]
ind_pak_ban. head ()
ind_pak_ban.T
ind_pak_ban.T.plot ()
plt. show()


# group the number of immigrants, to sum up, the total number of immigrants for each continent
cont = df. groupby ('Continent', axis=0).sum ()
cont['Total'].plot(kind='pie', figsize=(7, 7),
                   autopct='%1.1f%%',
                   shadow=True)
plt.title('Immigration By Continents')
plt.axis('equal')
plt.show()

#Immigrants data of China to a box plot
china = df.loc[[ 'China'], years].T
china.plot(kind='box', figsize= (8, 6)) 
plt.title ('Box plot of Chinese Immigrants') 
plt.ylabel ('Number of Immigrants') 
plt. show ()

# box plots of the number of immigrants of India, Pakistan and Bangladesh
ind_pak_ban.T.plot(kind='box', figsize= (8, 7))
plt.title('Box plots of Indian, Pakistan and Bangladesh Immigrants') 
plt.ylabel ('Number of Immigrants') 
plt.show ()

#scatter plot
# make a new DataFrame that will contain the years as an index and the total number of immigrants each year
totalPerYear = pd.DataFrame (df[years].sum(axis=0))
totalPerYear.head ()
print (totalPerYear.head ())
# need to convert the years to integers and polish the DataFrame to make it presentable
totalPerYear.index = map(int, totalPerYear.index)
totalPerYear.reset_index(inplace=True)
totalPerYear.head()
print(totalPerYear.head())


#area plot
# make Dataframe including the information of India, China, Pakistan, and France.
top = df.loc[['India', 'China', 'Pakistan', 'France'], years]
top = top.T
print (top)

colors = ['Black', 'Green', 'Blue', 'Red']
top.plot(kind='area', stacked=False, figsize=(20, 10)) 
plt.title('Immigration trend from Europe')
plt.ylabel('Number of Immigrants') 
plt.xlabel('Years') 
plt.show ()


# Histogram to show immigration from India, China, Pakistan, and France
top.plot.hist()
plt.title('Histogram of Immigration from Some Populous Countries')
plt.ylabel('Number of Years')
plt.xlabel ('Number of Immigrants')


# Improving the histogram by specify the number of bins and find out the bin edges
count, bin_edges = np.histogram(top, 15)
top.plot(kind='hist', figsize=(14, 6), bins=15, alpha=0.6,
xticks=bin_edges, color=colors)
plt.show()


# Histogram with "staked" feature
top.plot(kind='hist',
figsize=(12, 6), 
bins=15, 
xticks=bin_edges, 
color=colors, 
stacked=True,
)
plt.title('Histogram of Immigration from Some Populous Countries')
plt.ylabel('Number of Years')
plt.xlabel('Number of Immigrants')
plt.show ()


# Bar plot for the number of immigrants from France per year
france = df.loc['France', years]
france.plot(kind='bar', figsize=(10, 6)) 
plt.xlabel('Year')
plt.ylabel ('Number of immigrants')
plt.title('Immigrants From France')



# Increasing trend since 1997 for over a decade using an annotate function
france.plot(kind='bar', figsize=(10, 6)) 
plt.xlabel('Year') 
plt.ylabel('Number of immigrants') 
plt.title ('Immigrants From France') 
plt.annotate('Increasing Trend',
              xy=(19, 4500), 
              rotation=23, 
              va='bottom',
              ha='left')
plt.annotate('',
             xy=(29, 5500),
             xytext=(17, 3800), 
             xycoords='data', 
             arrowprops=dict(arrowstyle='->' , connectionstyle='arc3', color='black', lw=1.5))


# Horizontal bar reprentation
df_top10 = pd.DataFrame(df.nlargest(10, 'Total') ['Total'].sort_values(ascending=True))

df_top10.plot.barh(legend=False, color='crimson', edgecolor= 'LightCoral') 
plt.title('Top 10 Immigrant Countries to Canada from 1980-2013', color='black') 
plt.xlabel('Number of Immigrants', color='black') 
plt.ylabel('Country', color='black') 
plt.xticks(color='black' ) 
plt.yticks(color='black')

 
''' Q01 - Improve the appearance of the pie plot we did in step 4 of the plotting exercise
subsection. First, choose the colors as light green, light blue, pink, purple, grey, and gold.
Second, set the explode attribute. Finally, set the starting angle of the pie plot to any value
from 0 to 360 accordingly.'''

# group the number of immigrants, to sum up, the total number of immigrants for each continent
cont = df.groupby ('Continent', axis=0).sum ()
cont['Total'].plot(kind='pie', figsize=(7, 7),
                   autopct='%1.1f%%',
                   colors = ['lightgreen', 'lightblue', 'pink', 'purple','grey', 'gold'],
                   explode = [0.1,0.1,0.1,0.1,0.1,0.1],
                   startangle = 90,
                   shadow=True)
plt.title('Immigration By Continents')
plt.axis('equal')
plt.show()

'''Q02 - Produce a scatter plot using the DataFrame in step 7 of the plotting exercise
subsection to see the trend in the number of immigrants to Canada over the years.'''

# make a new DataFrame that will contain the years as an index and the total number of immigrants each year
totalPerYear = pd.DataFrame(df[years].sum(axis=0))
totalPerYear.head ()
print (totalPerYear.head ())

# need to convert the years to integers and polish the DataFrame to make it presentable
totalPerYear.index = map(int, totalPerYear.index)
totalPerYear.reset_index(inplace=True)
totalPerYear.head()
print(totalPerYear.head())

totalPerYear.rename(columns={'index': 'years', 0: 'total'}, inplace=True)
print(totalPerYear.columns)

# For the scatter plot, specify the x-axis and y-axis for the scatter plot
totalPerYear.plot(kind='scatter',x='years', y='total', figsize=(10, 6), color='Red')
plt.title('Total Immigration')
plt.xlabel('Year')
plt.ylabel('Number of Immigrants')
plt.show()


'''Q03 - Produce an area plot using the “top” DataFrame in step 8 of the plotting exercise
subsection to see the individual countries' area plot. This can be done using the “stacked”
feature enabled i.e. set the value for the “stacked” feature as “True”.'''

top = df.loc[['Brazil', 'Germany', 'Ireland', 'France'], years]
top = top.T
print(top)
colors = ['Grey', 'Green', 'Blue', 'Red']
top.plot(kind='area', stacked=True, figsize=(20, 10), color = colors)
plt.title('Immigration trend from Europe') 
plt.ylabel('Number of Immigrants') 
plt.xlabel('Years')
plt. show()


'''Q04 - Compare the number of Icelandic immigrants (country = 'Iceland') to Canada from
the year 1980 to 2013 using a vertical bar plot. Explain in a maximum of five-line how
you did it and what do you understand from looking at the output.'''

iceland = df.loc['Iceland', years]
france.plot(kind='bar', figsize=(10, 6)) 
plt.xlabel('Year')
plt.ylabel ('Number of immigrants')
plt.title('Immigrants From Iceland')
iceland.head()

iceland.plot(kind='bar', figsize=(10, 6)) 
plt.xlabel('Year') 
plt.ylabel('Number of immigrants') 
plt.title ('Immigrants From Iceland') 
plt.annotate('Increasing Trend',
              xy=(19, 4500), 
              rotation=23, 
              va='bottom',
              ha='left')
plt.annotate('',
             xy=(29, 5500),
             xytext=(17, 3800), 
             xycoords='data', 
             arrowprops=dict(arrowstyle='->' , connectionstyle='arc3', color='black', lw=1.5))


'''Q05 - Produce a horizontal bar plot showing the total number of immigrants to Canada
from the top 15 countries, for the period 1980 - 2013. Label each country with the total
immigrant count using the scripting layer. Explain in a maximum of five-line how you
did it and what do you understand from looking at the output.
References'''

df_top15 = pd.DataFrame(df.nlargest(15, 'Total')['Total'].sort_values(ascending=True))

top15 = df_top15.plot.barh(legend=False, color='crimson', edgecolor='LightCoral') 

for country, value in zip(df_top15.index, df_top15['Total']):
    top15.text(value, df_top15.index.get_loc(country), f'{value:,}', color='black', ha='left', va='center')


plt.title('Top 15 Immigrant Countries to Canada from 1980-2013', color='black') 
plt.xlabel('Number of Immigrants', color='black') 
plt.ylabel('Country', color='black')
plt.xticks(color= 'black')
plt.yticks(color='black')

