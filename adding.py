import pandas as pd
employee={
    'Name':['Umesh','Bijay','Samriddha','Aayush','Suan','Shyam','Khagendra'],
    'Age':[35,23,42,22,55,25,59],
    'Salary':[80000,19500,18300,27500,23900,34000,41000],
    'Performance':[82,88,72,90,95,80,79]
}
df=pd.DataFrame(employee)
print(df)
#adding column using straight forward method
df['Bonus']=df['Salary']*0.1
print(df)

#add column using insert()
#insert takes three values 1.location ,2.column name, 3.data
df.insert(0,'Employee ID',[101,102,103,104,105,106,107])
print("\nData added using insert\n")
print(df)

#Note :when to use insert and when to use straight forward method
#if the position of the data inside the data set doesnt matter then you can use straight forward method
#and if the position have to be specific then insert is used