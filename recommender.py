import pandas as pd

# Load fund scorecard
funds = pd.read_csv("data/processed/fund_scorecard.csv")

print("Fund data loaded successfully!")
print("\nRisk Appetite Options:")
print("1. Low")
print("2. Moderate")
print("3. High")

choice = input("\nEnter your choice (Low/Moderate/High): ").strip().lower()

if choice == "low":

    recommended = funds.sort_values(
        ["sharpe_ratio_y", "maximum_drawdown"],
        ascending=[False, True]
    ).head(3)

elif choice == "moderate":

    recommended = funds.sort_values(
        ["alpha_y", "sharpe_ratio_y"],
        ascending=[False, False]
    ).head(3)

elif choice == "high":

    recommended = funds.sort_values(
        "return_5yr_pct",
        ascending=False
    ).head(3)

else:
    print("Invalid choice!")
    exit()

print("\nTop 3 Recommended Funds\n")

print(
    recommended[
        [
            "scheme_name",
            "category",
            "return_5yr_pct",
            "sharpe_ratio_y",
            "alpha_y"
        ]
    ]
)