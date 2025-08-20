"""
Employee Performance Data Analysis Script
Author: OpenAI ChatGPT
Contact: 24f1001831@ds.study.iitm.ac.in
"""

import pandas as pd
import numpy as np
import plotly.express as px

# Step 1: Generate synthetic employee performance data and save as CSV
np.random.seed(42)
departments = ["Sales", "HR", "IT", "Finance", "Marketing"]
regions = ["North", "South", "East", "West"]

data = {
    "Department": np.random.choice(departments, 200),
    "Region": np.random.choice(regions, 200),
    "Performance_Score": np.random.randint(50, 100, 200),
}

df = pd.DataFrame(data)
df.to_csv("employee_performance.csv", index=False)

# Step 2: Load data
df = pd.read_csv("employee_performance.csv")

# Step 3: Frequency count for 'Sales' department
sales_count = df[df["Department"] == "Sales"].shape[0]
print(f"Number of employees in Sales department: {sales_count}")

# Step 4: Create histogram of department distribution
fig = px.histogram(df, x="Department", title="Department Distribution")

# Step 5: Save histogram visualization as HTML
fig.write_html("department_distribution.html")

print("Analysis complete. Histogram saved as 'department_distribution.html'")
