import pandas as pd 
import numpy as np
df = pd.read_csv("C:/Users/user/OneDrive/Desktop/ai_business_intelligence/raw_data/sales_data.csv", encoding = "latin1" )
print (df.head())

# check info of the table
df.info()

print(df.describe())

# converts column names into lower case and removed space

df.columns = df.columns.str.lower()
df.columns = df.columns.str.strip()

# replace white space with underscore using replace function
print(df.columns)
df.columns = df.columns.str.replace(" ", "_")
print(df.columns)

#fill sales, profit, discount and region using mean, mode, median
print(df.isnull().sum())
df['sales'].fillna(df['sales'].mean(),inplace=True)
df['profit'].fillna(df['profit'].median(), inplace=True)
df['discount'].fillna(0,inplace=True)
df['region'].fillna(df['region'].mode(), inplace=True)

print(df.head())

# change data type 
df['postal_code'] = df['postal_code'].astype(str)

# fill postcode using these functions
df['postal_code'] = df.groupby('city')['postal_code'].transform(lambda x: x.fillna(x.mode()[0] 
if not  x.mode().empty else "unknown"))
print(df.isnull().sum())

# fill dates using these functions
df['order_date']= df['order_date'].ffill()
df['ship_date'] = df['ship_date'].bfill()

# remove duplicates
print (df.duplicated().sum())
df.drop_duplicates(inplace = True)

# change data type and convert to lower case
df ['region'] = df['region'].str.lower().str.strip()
df ['category'] = df ['category'].str.lower().str.strip()
df['sales'] = pd.to_numeric(df ['sales'], errors= 'coerce')
df ['quantity'] = df ['quantity'].astype(int)
df ['customer_name'] = df ['customer_name'].astype(str)

# convert date into real dates 
df['order_date'] = pd.to_datetime(
    df['order_date'],
    format='mixed',
    dayfirst=True,
    errors='coerce'
)

df['ship_date'] = pd.to_datetime(
    df['ship_date'],
    format='mixed',
    dayfirst=True,
    errors='coerce'
)

df['order_date'] = df['order_date'].ffill().bfill()
df['ship_date'] = df['ship_date'].ffill().bfill()

df.rename(columns={ 'sub-category' : 'sub_category'}, inplace=True)
print(df.columns)

print(df['sales'].describe())

# IQR method for finding outliers and  fixing

Q1= df['sales'].quantile(0.25)
Q3= df['sales'].quantile(0.75)
IQR = Q3-Q1
df = df[
    (df['sales'] >= Q1 - 1.5 * IQR) &
    (df['sales'] <= Q3 + 1.5 * IQR)
]

# new columns 

df['profit_margin'] = df['profit'] / df['sales']
df['shipping_delay'] = (df['ship_date'] - df['order_date']).dt.days
df['sales_segment'] = df['sales'].apply(lambda x: 'high' if x > 500 
 else ('medium' if x >200 else 'low' ))

print(df.columns)

print(df.isnull().sum())
print(df[['order_date', 'ship_date']].isnull().sum())
print(df[['order_date', 'ship_date', 'shipping_delay']].isnull().sum())

print(df['order_date'])

print(df.isnull().sum())
print(df.info())
df['shipping_delay'] = pd.to_numeric(df['shipping_delay'], errors='coerce')

df.to_csv(
    "C:/Users/user/OneDrive/Desktop/ai_business_intelligence/cleaned_data/cleaned_sales_data.csv",
    index=False
)