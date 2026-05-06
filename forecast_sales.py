import pandas as pd
from prophet import Prophet
from sqlalchemy import create_engine
import matplotlib.pyplot as plt

# Connect to MySQL
engine = create_engine(
    "mysql+pymysql://root:root@localhost:3306/ai_business_intelligence"
)

# Load sales data
df = pd.read_sql(
    "SELECT order_date, sales FROM sales_data",
    con=engine
)

# Group daily sales
daily_sales = df.groupby("order_date")["sales"].sum().reset_index()

# Rename for Prophet
daily_sales.columns = ["ds", "y"]

# Create model
model = Prophet()

# Train model
model.fit(daily_sales)

# Future dates
future = model.make_future_dataframe(periods=90)

# Predict
forecast = model.predict(future)

# Save forecast CSV
forecast.to_csv(
    "C:/Users/user/OneDrive/Desktop/ai_business_intelligence/ai_reports/sales_forecast.csv",
    index=False
)

# Plot forecast
model.plot(forecast)

# Save forecast chart
plt.savefig("C:/Users/user/OneDrive/Desktop/ai_business_intelligence/ai_reports/sales_forecast_chart.png")

print("Sales forecasting completed successfully.")