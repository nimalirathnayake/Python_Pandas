# Description: Introduction to pandas and Data transformation to python
#Author: Nimali Rathnayake
#Date: 11-1-23

#Import module and data
import pandas as pd

df_raw = pd.read_csv('https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv')
# Examining df_raw(dataset)

type(df_raw)
df_raw.shape
df_raw.columns

#subset our data
keep =['country', 'year', 'iso_code', 'population', 'gdp', 'co2','methane', 'nitrous_oxide']
df = df_raw[keep]

#remove early patchy data
#df.year mean access year variable

df = df[df.year >= 1900]

# remove late patchy data
df = df[df.year < 2019]

#check your subsetting has worked
min(df.year)
max(df.year)

#examining the variables

df.dtypes

df.describe()
# Commnad gives information about specific statistics or datatype
df.co2.describe()
df.country.describe()

#cleaning the data
df[df.co2 == df.co2.max()]


#1 Look at the iso_code
df.iso_code

#df.iso_code.isna().mean givesanswer for step 2

#2 Identify NaNs
df.iso_code.isna()

#3 Check entries to remove
df[df.iso_code.isna()].country.unique() #what are the NaN countries

#4 Remove NaNs from iso_code
df = df[df.iso_code.notna()]

df.country.unique()

# Adding columns
df.columns

# New column

df['co2e'] = df[['co2', 'methane','nitrous_oxide']].sum (axis = 1)

df.columns
# per capita columns
df['co2e_pc'] = df.co2e / df. population
df['gdp_pc'] = df.gdp / df.population


# Merging datasets


#read new data

spi = pd.read_csv ('https://gist.githubusercontent.com/stragu/57b0a0750678bada09625d429a0f806b/raw/a18a454d7d225bd24074399a7ab79a4189e53501/spi.csv')

spi.shape
spi.column

#Merge data frame

df_all = pd.merge(df, spi, 
                  how = 'left',
                  left_on = ['iso_code', 'year'],
                  right_on = ['country_code', 'year'])

df_all.columns
df_all.year

# Remove unnecessary variables using pop method

df_all.pop('country_code')

df_all.spi.mean()

#Create summaries

spi_sum = df_all.groupby('country').spi.agg('mean').sort_values(ascending = False)

# Output / writing data

spi_sum.to_csv('spi_summary.csv')

# Brief visualisation

df_all.plot(x = 'co2e_pc', y = 'spi') # Line plot
df_all.plot(x = 'co2e_pc', y = 'spi', kind = 'scatter') # Scatter plot

# subset for 2016
df_all[df_all.year == 2016].plot (x = 'co2e_pc',
                                  y = 'spi',
                                  kind = 'scatter' )
# add a third variable using colour

df_all[df_all.year == 2016].plot (x = 'co2e_pc',
                                  y = 'spi',
                                  c = 'gdp_pc',
                                  colormap = 'viridis',
                                  kind = 'scatter' )
# change x and y lables

df_all[df_all.year == 2016].plot (x = 'co2e_pc',
                                  y = 'spi',
                                  c = 'gdp_pc',
                                  colormap = 'viridis',
                                  kind = 'scatter',
                                  xlabel = 'GHG per capita (MT co2e/yr)', 
                                  ylabel =  'social progress',
                                  sharex = False)




x= input()
y = input()
print(x+y) 










 