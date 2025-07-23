import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

#loading the dataset 
df = pd.read_csv('sales_data_100.csv')
print (df.head())
print ("Original data set : ")
print (df.head())

#step 2 convert 'date' to date time format 
df['Date'] = pd.to_datetime(df['Date'])

#Need to add Randot Unit price (missing value)
#col -- simulated
np.random.seed(42)
df['Unit_price'] = np.random.randint(10000,60000,size=len(df))

#Add a random store col into the dataset
stores = ['Store_A', 'Store_B', 'Store_C',]
df['Store'] = np.random.choice(stores, size=len(df))

#create 'Total_sales' col
df['Total_sales'] = df['Units_Sold'] * df['Unit_price']

#basic info and stats
print ('\n Data info. ')
print (df.info)

print ('\n Summary Sat: ')
print (df.describe())

#total sales by store
sales_by_stores = df.groupby('Store')['Total_sales'].sum().sort_values(ascending=False)
print ('\n Total Sales by Stores: ')
print (sales_by_stores)

#Total sale by product 
sales_by_product = df.groupby('Product')['Total_sales'].sum().sort_values(ascending=False)
print ('\n Total Sales by Product: ')
print (sales_by_product)

#Total sale by Region 
sales_by_region = df.groupby('Region')['Total_sales'].sum().sort_values(ascending=False)
print ('\n Total Sales by Region: ')
print (sales_by_region)

#monthly sales 
df['Month'] = df['Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Total_sales'].sum()
print ('\n Monthly Sales: ')
print(monthly_sales)

#Sales by Store
plt.figure(figsize=(10,12))
sales_by_stores.plot(kind = 'bar', color='Coral')
plt.title('Total Sales by Store')
plt.xlabel('Store')
plt.ylabel('Sales(in $)')
plt.grid(True)
plt.tight_layout()
plt.show()

#2nd plot
plt.figure(figsize=(7,8))
sales_by_product.plot(kind ='bar', color='Cyan')
plt.title('Total Sales by Product')
plt.xlabel('Product')
plt.ylabel('Sales(in $)')
plt.grid(True)
plt.tight_layout()
plt.show()

#Sales by Region pie chart 
plt.figure(figsize=(10,12))
sales_by_region.plot(kind='pie', autopct='%1.1f%%')
plt.title('Total Sales by Region')
plt.tight_layout()
plt.show()