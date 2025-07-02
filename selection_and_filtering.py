import pandas as pd
employee={
    'Name':['Umesh','Bijay','Samriddha','Aayush','Suan','Shyam','Khagendra'],
    'Age':[35,23,42,22,55,25,59],
    'Salary':[80000,19500,18300,27500,23900,34000,41000],
    'Performance':[82,88,72,90,95,80,79]
}
df=pd.DataFrame(employee)
print(df)
#selecting the single column returns the series
print('\nSelecting the single column name\n')
name=df['Name']
print(name)

#selecting multiple columns
#selecting the multiple column returns the dataframe
#lets select the name and the age col
multiple=df[['Name','Age']]
print(multiple)

#Now filtering based on  salary column in which salary greater than 30000
sal=df[df['Salary']>30000] #this code check the boolen function if the value is true it prints the entire row 
print(sal)

print('\nName of the employee having salary>30000\n')
sal1=df[df['Salary']>30000]['Name']#This code prints only the name of the employee having salary greater than 30000
#this print the name in seris if you want to print the name in dataframe use double square bracket [['Name']]
print(sal1)

#multiple conditions
#AND condition (&)
print('Details of employee having age>30 AND salary>30000') #display the employees having  both condition  true
emp=df[(df['Age']>30)&(df['Salary']>30000)]
print(emp)

#OR condition (|)
print('Details of employee having age>40 OR performance>85') #display the employees having only one condition true
emp1=df[(df['Age']>40)|(df['Performance']>85)]
print(emp1)