import pandas as pd

# Load cleaned NAV history
df = pd.read_csv("data/processed/nav_history_cleaned.csv")

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Sort by scheme and date
df = df.sort_values(by=["amfi_code", "date"])

# Calculate daily return for each AMFI scheme
df["daily_return"] = (
    df.groupby("amfi_code")["nav"]
    .pct_change()
)

# Remove first row of each scheme (daily_return = NaN)
df = df.dropna(subset=["daily_return"])

# Save to processed folder
output_path = "data/processed/daily_returns.csv"
df.to_csv(output_path, index=False)

print("=" * 50)
print("Daily Returns Calculation Completed")
print("=" * 50)
print(f"Total Records: {len(df)}")
print(f"Output File: {output_path}")
print("\nFirst 5 Rows:")
print(df.head())