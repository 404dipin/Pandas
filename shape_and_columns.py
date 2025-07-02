import pandas as pd
data={
    'Name':['Umesh','Bijay','Khagendra','Aayush'],
    'Age':[23,24,22,22],
    'Salary':[20000,25000,35000,22000],
    'Location':['Dhangadi','Ramechhap','Pyuthan','Dhapakhel']
}
df=pd.DataFrame(data)
print(f"Shape: {df.shape}") #gives the total no of rows and column in the dataframe
print(f"Coumns: {df.columns}")#gives the name of the columns present in the dataframe   
