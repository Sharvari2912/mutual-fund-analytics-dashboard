import pandas as pd

df = pd.read_csv("data/raw/07_scheme_performance.csv")

# Columns containing returns
return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct"
]

# Validate numeric returns
for col in return_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

    anomalies = df[df[col].isna()]

    print(f"{col} anomalies: {len(anomalies)}")

# Validate expense ratio
df["expense_ratio_pct"] = pd.to_numeric(
    df["expense_ratio_pct"],
    errors="coerce"
)

expense_anomalies = df[
    (df["expense_ratio_pct"] < 0.1) |
    (df["expense_ratio_pct"] > 2.5)
]

print("\nExpense Ratio Anomalies:")
print(expense_anomalies[
    ["amfi_code", "scheme_name", "expense_ratio_pct"]
])

# Convert remaining numeric columns
numeric_cols = [
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "aum_crore",
    "morningstar_rating"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Remove duplicate rows
df = df.drop_duplicates()

# Save cleaned data
df.to_csv(
    "data/processed/04_scheme_performance_cleaned.csv",
    index=False
)

print("\nCleaned Shape:", df.shape)
print("Cleaning Complete.")