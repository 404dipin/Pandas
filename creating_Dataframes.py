import pandas as pd
df=pd.read_excel("weather_data.xlsx")#pd.read_excel reads the excel file
#passed weather_data.xlsx as it is in the same directory/ the excel file is inside the pandas folder 
#if the folder is not inside the pandas folder then we have to specify the full path like this "D:\Pandas\weather_data.xlsx"
print(df)
#now lets take the data(dictionary) and convert them into the dataframe
data1={
    'day':['1/02/2025','1/03/2025'],
    'temp':[32,36],
    'wind_speed':[6,7],
    'event':['Rainy','Windy']
}
df1=pd.DataFrame(data1)
print(df1)

#now lets take the data (tupels) and convert them into dataframe
data2=[
    ('1/01/2082',32,2,'Rain'),
    ('1/02/2082',32,6,'Windy'),
    ('1/03/2082',32,4,'Sunny')
]
df2=pd.DataFrame(data2,columns=["day","temp","windspeed","Status"]) #we have to specify the columns in tupels
print(df2)