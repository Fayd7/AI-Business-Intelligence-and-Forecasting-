USE ai_business_intelligence;

-- Total Sales by Region
SELECT region, round(SUM(sales),2) AS total_sales
FROM sales_data
GROUP BY region
ORDER BY total_sales DESC;

-- Total Profit by Category
SELECT category, round(SUM(profit),2) AS total_profit
FROM sales_data
GROUP BY category
ORDER BY total_profit desc;

# Average Shipping Delay by Region
SELECT region,
    AVG(shipping_delay) AS avg_shipping_delay
FROM sales_data
GROUP BY region
ORDER BY avg_shipping_delay DESC;


# Top 10 Products by Sales
SELECT product_name,
    SUM(sales) AS total_sales
FROM sales_data
GROUP BY product_name
ORDER BY total_sales DESC
LIMIT 10;


# Sales Segment Distribution
SELECT sales_segment,
    COUNT(*) AS order_count
FROM sales_data
GROUP BY sales_segment;

# Monthly Sales Trends by Month Name
SELECT MONTH(order_date) AS month_number,
    MONTHNAME(order_date) AS month,
    SUM(sales) AS monthly_sales
FROM sales_data
GROUP BY MONTH(order_date), MONTHNAME(order_date)
ORDER BY month_number;

# Create Regional KPI Summary Table
DROP TABLE IF EXISTS regional_kpis;


CREATE TABLE regional_kpis (
    region VARCHAR(100),
    total_sales DECIMAL(15,2),
    total_profit DECIMAL(15,2),
    avg_delay DECIMAL(10,2)
);
INSERT INTO regional_kpis
SELECT
    region,
    SUM(sales),
    SUM(profit),
    AVG(shipping_delay)
FROM sales_data
GROUP BY region;

select * from regional_kpis;

# Count Total Records in Sales Data
SELECT COUNT(*) AS total_records
FROM sales_data;


# View Table Structure
DESCRIBE sales_data;

# Top Region by Profit
SELECT *
FROM regional_kpis
ORDER BY total_profit DESC;

# Worst Region by Shipping Delay
SELECT *
FROM regional_kpis
ORDER BY avg_delay DESC;

# Monthly Profit Trends
SELECT
    MONTH(order_date) AS month_number,
    MONTHNAME(order_date) AS month,
    SUM(profit) AS monthly_profit
FROM sales_data
GROUP BY MONTH(order_date), MONTHNAME(order_date)
ORDER BY month_number;

# Category-wise Sales and Profit
SELECT
    category,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit
FROM sales_data
GROUP BY category
ORDER BY total_sales DESC;

# Top 5 Customers by Sales
SELECT
    customer_name,
    SUM(sales) AS total_sales
FROM sales_data
GROUP BY customer_name
ORDER BY total_sales DESC
LIMIT 5;

# Average Profit Margin by Region
SELECT
    region,
    AVG(profit_margin) AS avg_profit_margin
FROM sales_data
GROUP BY region
ORDER BY avg_profit_margin DESC;

# Shipping Delay by Ship Mode
SELECT
    ship_mode,
    AVG(shipping_delay) AS avg_shipping_delay
FROM sales_data
GROUP BY ship_mode
ORDER BY avg_shipping_delay DESC;