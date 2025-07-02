import pandas as pd
#head() and tail() by default display upto 5 rows from top and bottom respectively
#head(n) display the rows from the top to n
#tail(n) display the rows from the bottom to n
df=pd.read_csv('sales_data_sample.csv',encoding='latin1')
print("Display 10 rows from top ")
print(df.head(10))

print('Display 10 rows from bottom')
print(df.tail(10))
