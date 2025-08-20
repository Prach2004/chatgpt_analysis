import plotly.express as px
import pandas as pd

# -----------------------
# Dataset (with 12 "Sales")
# -----------------------
departments = [
    "Finance", "Marketing", "IT", "HR",
    "Sales", "Sales", "Sales", "Sales", "Sales", "Sales",
    "Sales", "Sales", "Sales", "Sales", "Sales", "Sales",  # 12 total
    "Finance", "Marketing", "IT", "HR", "Finance", "IT"
]

df = pd.DataFrame({"Department": departments})

# -----------------------
# Plotly Histogram
# -----------------------
fig = px.histogram(
    df,
    x="Department",
    title="Department Distribution"
)

# -----------------------
# Save HTML
# -----------------------
output_file = "output.html"
fig.write_html(output_file)

# -----------------------
# Extra info to inject
# -----------------------
roll_email = "24f1001831@ds.study.iitm.ac.in"
sales_count = (df["Department"] == "Sales").sum()

injection = f"""
<span style="display:none;">{roll_email}</span>
<h3 style="font-family:Arial; color:#333;">
    Roll Number / Email: {roll_email}
</h3>
<p><b>Frequency count for "Sales" department:</b> {sales_count}</p>
"""

# -----------------------
# Read back own script
# -----------------------
with open(__file__, "r", encoding="utf-8") as f:
    script_content = f.read()

code_block = f"""
<h3>Python Code Used:</h3>
<pre><code>{script_content}</code></pre>
"""

# -----------------------
# Modify HTML file
# -----------------------
with open(output_file, "r", encoding="utf-8") as f:
    html = f.read()

html = html.replace("</body>", injection + code_block + "</body>")

with open(output_file, "w", encoding="utf-8") as f:
    f.write(html)

print(f"✅ HTML file generated: {output_file}")
print(f"   'Sales' frequency = {sales_count}")
