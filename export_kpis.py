import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://root:root@localhost:3306/ai_business_intelligence"
)

regional_kpis = pd.read_sql(
    "SELECT * FROM regional_kpis",
    con=engine
)

regional_kpis.to_csv(
    "C:/Users/user/OneDrive/Desktop/ai_business_intelligence/ai_reports/regional_kpis_report.csv",
    index=False
)

print("KPI report exported successfully.")