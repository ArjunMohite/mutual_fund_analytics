import pandas as pd

df = pd.read_csv("data/raw/02_nav_history.csv")

# Parse date
df["date"] = pd.to_datetime(df["date"])

# Sort
df = df.sort_values(
    by=["amfi_code", "date"]
)

# Remove duplicates
df = df.drop_duplicates()

# Forward fill NAV
df["nav"] = (
    df.groupby("amfi_code")["nav"]
    .ffill()
)

# Keep valid NAV
df = df[df["nav"] > 0]

# Save
df.to_csv(
    "data/processed/nav_history_cleaned.csv",
    index=False
)

print(df.shape)
print("NAV cleaning complete")