import os
os.system("python clean_data.py")
os.system("python upload_to_mysql.py")
os.system("python export_kpis.py")
os.system("python generate_ai_insights.py")
print("Full AI Business Intelligence pipeline completed successfully.")