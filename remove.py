import pandas as pd
employee={
    'Name':['Umesh','Bijay','Samriddha','Aayush','Suan','Shyam','Khagendra'],
    'Age':[35,23,42,22,55,25,59],
    'Salary':[80000,19500,18300,27500,23900,34000,41000],
    'Performance':[82,88,72,90,95,80,79]
}
df=pd.DataFrame(employee)
print(df)
#lets drop/remove the preformance column
df.drop(columns=['Performance'],inplace=True)   
#here inplace =True modified the original dataframe
#if we use inplace=False then we get the new dataframe 
print("\n Modified Data\n")
print(df)