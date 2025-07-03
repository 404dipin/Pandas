import pandas as pd
employee={
    'Name':['Umesh','Bijay','Samriddha','Aayush','Suan','Shyam','Khagendra'],
    'Age':[35,23,42,22,55,25,59],
    'Salary':[80000,19500,18300,27500,23900,34000,41000],
    'Performance':[82,88,72,90,95,80,79]
}
df=pd.DataFrame(employee)
print(df)

#updating the data......
df.loc[0,'Salary']=90000
print("\n updated data\n")
print(df)

#updating the entire column salary
df['Salary']+=df['Salary']*0.1
print('\n After updating the entire column Salary\n')
print(df)