# -*- coding: utf-8 -*-
"""Predict_Weather(Easy).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SPemrZBr2Jc691DTgD9N7QYmTmPslH70

**Import the Libraries**
"""

import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

"""**Load the Dataset**"""

x = "weather_data.csv"

df = pd.read_csv(x)

"""**Inspect the Dataset**"""

# Display the first five rows of the Dataset

print(df.head())

# Check the data types of each column

print(df.info())

# Convert Date into a proper datetime format

df['timestamp_utc'] = pd.to_datetime(df['timestamp_utc'], format ='%Y-%m-%dT%H:%M:%S')

df['timestamp_local'] = pd.to_datetime(df['timestamp_local'], format ='%Y-%m-%dT%H:%M:%S')

df['datetime'] = pd.to_datetime(df['datetime'], format = '%Y-%m-%d:%H')

"""**Feature Engineering**"""

# Extract the Year, Month and Data and create new columns

df['Year'] = df['datetime'].dt.year

df['Month'] = df['datetime'].dt.month

df['Day'] = df['datetime'].dt.day

# Check the new columns

print(df['Year'].head(3))

print(df['Month'].head(3))

print(df['Day'].head(3))

"""**Handling Null Values**"""

# Checking the null values in the Dataset

print(df.isnull().sum())

"""**Calculate basic statistics (mean, median, mode) for  Temperature, Humidity and Wind Speed**

"""

print(df[['temp', 'rh', 'wind_spd']].agg(['mean', 'median', lambda x: x.mode()[0]]))

"""**Day with the Highest Temperature Recorded**"""

# Find the maximum temperature

max_temp = df['temp'].max()

print(max_temp)

# Find the day with the maximum temperature

maxtemp_day = df[df['temp'] == max_temp]['Day'].iloc[0]

print(maxtemp_day)

"""**Identify the most frequent Weather Condition in the dataset**"""

# Get the most frequent weather condition

most_frq_weather = df['description(output)'].mode()[0]

print("Most frequent weather condition: ", most_frq_weather)

# Get the count of most frequent weather condition

count = df['description(output)'].value_counts()[most_frq_weather]

print("Count: ", count)

"""**Count the number of Clear Sky and Drizzle days**"""

# Count of 'Clear Sky' Days

count_sunny = df['description(output)'].value_counts()['Clear Sky']

print(f"Count of 'Clear Sky' days: {count_sunny}")

# Count of 'Drizzle' Days

count_drizzle = df['description(output)'].value_counts()['Drizzle']

print(f"Count of 'Drizzle' Days: {count_drizzle}")

"""**Average wind speed on 'Light shower rain' day**"""

# Filter out the Light Shower Rain days

rain_day = df[df['description(output)'] == 'Light shower rain']

# Calculate average wind speed on rainy day

avg_speed = rain_day['wind_spd'].mean()

print(f"Average wind speed on 'Light shower rain' day is: {avg_speed}")

"""**Filter out records where the temperature was below 30°C**"""

# Filter records where temperature is below 20°C

temp_below_20 = df[df['temp'] < 30]


# Get the count of records

count = temp_below_20['temp'].count()


print(f"Records where the temperature was below 30°C is {count}")

"""**Plot a histogram of Temperature**"""

plt.hist(df['temp'], bins = 20, color = 'skyblue', edgecolor = 'black')

plt.xlabel('Tempearute (°C)')

plt.ylabel('Frequency')

plt.title('Histogram of Temperature')

plt.show

"""**Create a Scatter Plot of Temperature vs. Humidity**"""

sns.scatterplot(x = 'temp', y = 'rh', data = df, color = 'orange')

plt.xlabel('Tempearute (°C)')

plt.ylabel('Humidity (%)')

plt.title('Temperature v/s Humidity')

plt.show

"""**Create a Line Plot of Temperature Over Time**"""

plt.figure(figsize = (10,6))

plt.plot(df['timestamp_utc'], df['temp'], color = 'green', linewidth = 2)

plt.xlabel('Date')

plt.ylabel('Tempearute (°C)')

plt.title('Temperature Over Time')

plt.show()

"""**Create a Bar Plot Showing Number of Days per Weather Condition**"""

weather_count = df['description(output)'].value_counts()

plt.figure(figsize = (8,6))

weather_count.plot(kind = 'bar', color = 'purple')

plt.xlabel('Weather Condition')

plt.ylabel('Number of Days')

plt.title('No. of Days per Weather Condition')

plt.show()

"""**Plot a Boxplot for Wind Speed to Detect Outliers**"""

plt.figure(figsize = (8,6))

sns.boxplot(x = df['wind_spd'], color = 'lightcoral')

plt.xlabel('Wind Speed km/hr')

plt.title('Boxplot of Wind Speed')

plt.show()