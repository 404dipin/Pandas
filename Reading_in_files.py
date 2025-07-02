import pandas as pd
df=pd.read_csv(r"D:\Pandas\countries of the world.csv") # reading the csv file
print(df)

df1=pd.read_table(r"D:\Pandas\countries of the world.txt")# reading the txt file
print(df1)

df2=pd.read_json(r"D:\Pandas\json_sample.json")#reading the json file
print(df2)


df3=pd.read_excel(r"D:\Pandas\world_population_excel_workbook.xlsx")
print(df3)
print(df3.info())