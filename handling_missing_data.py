import pandas as pd
employee={
    'Name':['Umesh',None,'Samriddha','Aayush','Suan','Shyam','Khagendra'],
    'Age':[35,None,42,22,55,25,59],
    'Salary':[80000,None,18300,27500,23900,34000,41000],
    'Performance':[82,None,72,90,95,80,79]
}
df=pd.DataFrame(employee)
print(df)

#to handle missing data either we remove the missing data or we fill the missing data.
#to remove the missing data we use dropna().
#to fill the missing data we use fillna().

# df.dropna(inplace=True)
#it removes the null value
# print("\n After dropping the null value\n")
# print(df)

df.fillna(0,inplace=True)
#it fills the null value
print(df)


