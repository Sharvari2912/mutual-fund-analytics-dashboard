import pandas as pd

# Read fund master dataset
df = pd.read_csv("data/raw/01_fund_master.csv")

# Unique Fund Houses
print("Unique Fund Houses:")
print(df["fund_house"].unique())

# Categories
print("\nCategories:")
print(df["category"].unique())

# Sub Categories
print("\nSub Categories:")
print(df["sub_category"].unique())

# Risk Categories
print("\nRisk Categories:")
print(df["risk_category"].unique())

# AMFI Scheme Code Structure Notes
print("\nTotal Schemes:", len(df))
print("Unique AMFI Codes:", df["amfi_code"].nunique())

print("\nSample AMFI Codes:")
print(df["amfi_code"].head())