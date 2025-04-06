import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import csv

df = pd.read_csv('data1.csv')
print("First 5 rows:")
print(df.head())
print(df.tail())

print("\nDataset information:")
print(df.info())

print("\nMissing values:")
print(df.isna().sum())

age_median = np.nanmedian(df['Age'])
print(age_median)

#Using fillna to fill missing values
df['Age'] = df['Age'].fillna(age_median)

#convert gender to numeriacal
df['Gender'] = df['Gender'].map({'Male':0,'Female':1})
print(df['Gender'].head())

#drop columns
df = df.drop(columns=['Work Pressure','Job Satisfaction'])
print(df.columns)

#Basic statistics with numpy
print("\nBasic statistics:")
print("Mean:",np.mean(df['Age']))
print("Median:",np.median(df['Depression']))
print("Standard Deviation:",np.std(df['Age']))

#Filtering data
print(df[(df['Age'] > 30) & (df['Depression'] == 1)][['City', 'Work/Study Hours', 'Age']])

#Pivot tables
pivot = pd.pivot_table(df,
                       index='Degree',
                       columns='Gender',
                       values='Depression',
                       aggfunc='mean')

print("\nDepression rate by Degree and Gender:")
print(pivot)

pivot1 = pd.pivot_table(df,
                        index = 'Degree',
                        columns = 'Gender',
                        values = 'CGPA',
                        aggfunc = 'mean')
print(pivot1)

#data visualization
plt.figure(figsize=(10, 5))
plt.hist(df[df['Depression']==1]['Age'], bins=20, color='red',alpha = 0.6)
plt.hist(df[df['Depression']==0]['Age'], bins=20, color='green',alpha = 0.6)
plt.title('Age Distribution by depression status')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()

#Seaborn barplot
plt.figure(figsize=(8, 4))
sns.barplot(x='Degree', y='Depression', data=df)
plt.title('Depression Rate by Gender')
plt.show()


#scatter plot
plt.figure(figsize=(8, 4))
sns.scatterplot(x='Age', y='CGPA', hue='Depression', data=df)
plt.title('Age vs CGPA (Colored by Depression Status)')
plt.xlabel('Age')
plt.ylabel('CGPA')
plt.show()


age_mean = np.mean(df['Age'])
age_std = np.std(df['Age'])
df['Age_zscore'] = (df['Age'] - age_mean) / age_std
print(df['Age_zscore'])

ages = df['Age'].values
young_adults = df[np.logical_and(ages >= 18, ages <= 25)]
print("\nNumber of young adults (18–25):", len(young_adults))
depressed_young = young_adults[young_adults['Depression'] == 1]
print("Number of depressed young adults:", len(depressed_young))
