#in this we learn about how the manipulated data is saved in pandas
import pandas as pd
data={
    'Name':['shyam','Umesh','Bijay'],
    'Age':[24,23,23],
    'city':['Accham','Dhangadi','Ramechhap']
}
#now we have a data of name, age and city 
#now creating the dataframe of the data
df=pd.DataFrame(data)
print(df)

#now saving  the data_frame into csv file
df.to_csv('Output.csv',index=False)
#index=false removes the indexing of the data

#saving the data_frame into excel file
df.to_excel('Output.xlsx',index=False)

#saving the data_frame into Json file
df.to_json('Output.json',index=False)