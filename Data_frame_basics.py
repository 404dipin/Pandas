import pandas as pd
#reading the data frame using pd.read_excel(location)
df=pd.read_excel(r"D:\Pandas\weather_data.xlsx")
print(df)

#creating the dataframe of the python dictionary data
weather={
    'day':['1/1/2025','1/2/2025'],
    'temperature':[32,35],
    'wind_speed':[6,4],
    'event':['rain','sunny']
}
df1=pd.DataFrame(weather)
print(df1)
print()
rows,column=df.shape
print(rows)
print()
print(column)

print(df.head())#prints the first 5 rows and also you can also pass the value to print
print(df.head(3)) #prints the first three rows

print(df.tail()) #prints the last 5 rows 

#slicing 
print("slicing",df[2:5])

#printing columns
print(df.columns)#prints the columns

print(df.Day) #prints the day column same for the other columns also and also we can use df['day']
