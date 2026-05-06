import pandas as pd

df= pd.read_csv("C:/Users/user/OneDrive/Desktop/ai_business_intelligence/ai_reports/regional_kpis_report.csv")


top_region = df.loc[df['total_profit'].idxmax()]
worst_region = df.loc[df['avg_delay'].idxmax()]

summary = f"""
Top Region:
{top_region['region']} generated the highest profit of {top_region['total_profit']:.2f}.

Operational Risk:
{worst_region['region']} has the highest shipping delay of {worst_region['avg_delay']:.2f}.
"""

with open("C:/Users/user/OneDrive/Desktop/ai_business_intelligence/ai_reports/executive_summary.txt", "w") as file:
    file.write(summary)

print("AI summary generated.")



