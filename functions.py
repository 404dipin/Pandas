import pandas as pd
#reading the data frame using pd.read_excel(location)
df=pd.read_excel(r"D:\Pandas\weather_data.xlsx")
print(df['Temperature'].max()) #max_value
print(df['Temperature'].mean())#mean/average_value
print(df['Temperature'].min())#minimum_value
print(df['Temperature'].std())#Standard deviation value

print(df.describe())#prints the statistics of the datasets.

#conditional statement
print(df.Temperature[df.Temperature>=30])
print(df[df.Temperature==df.Temperature.max()])
print(df[['Day','Temperature']][df.Temperature==df.Temperature.max()])

print(df.index)