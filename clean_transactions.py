import pandas as pd

df = pd.read_csv("data/raw/08_investor_transactions.csv")

# Standardize transaction types
df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.title()
)

mapping = {
    "Sip": "SIP",
    "Lumpsum": "Lumpsum",
    "Redemption": "Redemption"
}

df["transaction_type"] = df["transaction_type"].replace(mapping)

# Amount validation
df = df[df["amount_inr"] > 0]

# Date formatting
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"],
    errors="coerce"
)

# Check KYC
print(df["kyc_status"].unique())

df.to_csv(
    "data/processed/03_investor_transactions_cleaned.csv",
    index=False
)

print(df.shape)