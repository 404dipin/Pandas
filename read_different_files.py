#if you get the error in reading the file you can use either encoding='utf-8' or use encoding='latin1'
import pandas as pd
df=pd.read_csv("sales_data_sample.csv",encoding="latin1") #reading the csv file

print(df)
print()

df1=pd.read_excel("SampleSuperstore.xlsx") #reading the excel file
print(df1)
print()

#reading the json file
df2=pd.read_json('sample_Data.json')
print(df2)

#if your file is stored in the cloud then you can use gcfs library to read that file