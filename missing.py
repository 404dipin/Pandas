import pandas as pd
employee={
    'Name':['Umesh',None,'Samriddha','Aayush','Suan','Shyam','Khagendra'],
    'Age':[35,None,42,22,55,25,59],
    'Salary':[80000,None,18300,27500,23900,34000,41000],
    'Performance':[82,None,72,90,95,80,79]
}
df=pd.DataFrame(employee)
print(df)

print(df.isnull())# it returns the boolean value 


print(df.isnull().sum()) #it returns the value that is null and in which column also
