import pandas as pd

df = pd.read_csv("data/raw/08_investor_transactions.csv")

# Standardize transaction types
df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.title()
)

# Valid transaction types
valid_types = [
    "Sip",
    "Lumpsum",
    "Redemption"
]

df = df[
    df["transaction_type"]
    .isin(valid_types)
]

# Amount must be positive
df = df[df["amount_inr"] > 0]

# Convert dates
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"]
)

# Valid KYC values
valid_kyc = [
    "Verified",
    "Pending"
]

df = df[
    df["kyc_status"]
    .isin(valid_kyc)
]

# Remove duplicates
df = df.drop_duplicates()

# Save
df.to_csv(
    "data/processed/investor_transactions_cleaned.csv",
    index=False
)

print(df.shape)
print("Investor transactions cleaned")