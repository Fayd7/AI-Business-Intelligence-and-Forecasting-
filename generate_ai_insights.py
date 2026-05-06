import pandas as pd
from openai import OpenAI

client = OpenAI(api_key="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")
df = pd.read_csv("C:/Users/user/OneDrive/Desktop/ai_business_intelligence/ai_reports/regional_kpis_report.csv")

prompt = f"""
Analyze the following regional business KPI data:

{df.to_string(index=False)}

Provide:
1. Top business strengths
2. Operational risks
3. Strategic recommendations
4. Growth opportunities
"""

try:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    ai_summary = response.choices[0].message.content

except Exception as e:

    top_region = df.loc[df['total_profit'].idxmax()]
    worst_delay = df.loc[df['avg_delay'].idxmax()]

    ai_summary = f"""
GPT unavailable.

Fallback Executive Summary:

Top Performing Region:
{top_region['region']} generated the highest profit of {top_region['total_profit']:.2f}.

Operational Risk:
{worst_delay['region']} has the highest shipping delay of {worst_delay['avg_delay']:.2f} days.

Strategic Recommendation:
Focus on scaling profitable regions while addressing logistics inefficiencies in delayed markets.
"""

with open("C:/Users/user/OneDrive/Desktop/ai_business_intelligence/ai_reports/gpt_executive_summary.txt", "w") as file:
    file.write(ai_summary)

print("AI report generated successfully.")




