import pandas as pd
#describe method in pandas is a powerful tool that provides a summary of 
#descriptive statistics for numerical columns of your dataframes
data={
    'Name':['Umesh','Bijay','Khagendra','Aayush'],
    'Age':[23,24,22,22],
    'Salary':[20000,25000,35000,22000],
    'Location':['Dhangadi','Ramechhap','Pyuthan','Dhapakhel']
}
df=pd.DataFrame(data)
print(df.describe())
