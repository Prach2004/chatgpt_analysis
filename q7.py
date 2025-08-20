"""
Employee Performance Data Analysis Script
Author: OpenAI ChatGPT
Contact: 24f1001831@ds.study.iitm.ac.in
"""

import pandas as pd
import numpy as np
import plotly.express as px

# -------------------------------
# Step 1: Generate synthetic data
# -------------------------------
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

# -------------------------------
# Step 2: Load data
# -------------------------------
df = pd.read_csv("employee_performance.csv")

# -------------------------------
# Step 3: Frequency count for 'Sales' department
# -------------------------------
sales_count = df[df["Department"] == "Sales"].shape[0]
print(f"Number of employees in Sales department: {sales_count}")

# -------------------------------
# Step 4: Create histogram
# -------------------------------
fig = px.histogram(df, x="Department", title="Department Distribution")

# -------------------------------
# Step 5: Save histogram as HTML
# -------------------------------
html_file = "department_distribution.html"
fig.write_html(html_file, include_plotlyjs="cdn")

# -------------------------------
# Step 6: Inject roll number/email
# -------------------------------
with open(html_file, "r", encoding="utf-8") as f:
    html_content = f.read()

injection = f"""
<span style="display:none;">24f1001831@ds.study.iitm.ac.in</span>
<h3 style="font-family:Arial; color:#333;">
    Roll Number / Email: 24f1001831@ds.study.iitm.ac.in
</h3>
<p><b>Frequency count for "Sales" department:</b> {sales_count}</p>
"""


html_content = html_content.replace("<body>", f"<body>{injection}", 1)

with open(html_file, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"✅ Analysis complete. Histogram saved as '{html_file}' with roll number embedded.")
