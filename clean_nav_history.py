import pandas as pd

df = pd.read_csv("data/raw/02_nav_history.csv")

# Parse dates
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# Sort
df = df.sort_values(["amfi_code", "date"])

# Forward fill NAV
df["nav"] = df.groupby("amfi_code")["nav"].ffill()

# Remove duplicates
df = df.drop_duplicates()

# Keep only valid NAV values
df = df[df["nav"] > 0]

df.to_csv("data/processed/02_nav_history_cleaned.csv", index=False)

print(df.shape)