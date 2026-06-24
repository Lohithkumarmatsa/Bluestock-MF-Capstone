import pandas as pd

df = pd.read_csv("data/raw/07_scheme_performance.csv")

# Convert return columns to numeric
return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Flag anomalies
anomalies = df[
    (df["return_1yr_pct"] < -100) |
    (df["return_3yr_pct"] < -100) |
    (df["return_5yr_pct"] < -100)
]

print("Anomalies Found:", len(anomalies))

# Expense ratio validation
valid_expense = df[
    (df["expense_ratio_pct"] >= 0.1) &
    (df["expense_ratio_pct"] <= 2.5)
]

print("Valid Expense Ratio Records:", len(valid_expense))

# Save cleaned file
df.to_csv(
    "data/processed/07_scheme_performance_cleaned.csv",
    index=False
)

print("Cleaning completed successfully!")