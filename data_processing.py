import pandas as pd
import os

#LOAD DATA
#define paths to 3 files in 'data' folder
file_0 = "data/daily_sales_data_0.csv"
file_1 = "data/daily_sales_data_1.csv"
file_2 = "data/daily_sales_data_2.csv"

#read each file into a "DataFrame" (like virtual excel sheet)
df0 = pd.read_csv(file_0)
df1 = pd.read_csv(file_1)
df2 = pd.read_csv(file_2)

#combine all 3 to one table
df = pd.concat([df0, df1,df2])

#FILTER PINK MORSELS
#first clean the price (no $ sign for easy calc)
#multiply price and quantity
df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)
df['sales'] = df['price'] * df['quantity']

#CLEANUP COLUMNS
df = df[['sales', 'date', 'region']]

#SAVE OUTPUT new file
df.to_csv("formatted_output.csv", index=False)

print("Formatted file created!!")
