import pandas as pd
df=pd.read_json('sample_Data.json')
print("Displaying the info of data set")
print(df.info())

data={
    'Name':['shyam','Umesh','Bijay'],
    'Age':[24,23,23],
    'city':['Accham','Dhangadi','Ramechhap']
}
df1=pd.DataFrame(data)
print(df1.info())