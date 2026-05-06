import pandas as pd
from sqlalchemy import create_engine

# Load cleaned CSV
df = pd.read_csv(
    r"C:\Users\user\OneDrive\Desktop\ai_business_intelligence\cleaned_data\cleaned_sales_data.csv"
)

# MySQL connection
engine = create_engine(
    "mysql+pymysql://root:root@localhost:3306/ai_business_intelligence"
)

# Upload to MySQL
df.to_sql(
    "sales_data",
    con=engine,
    if_exists="replace",
    index=False
)

print("Data uploaded successfully!")