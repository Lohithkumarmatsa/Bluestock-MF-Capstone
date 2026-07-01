
import pandas as pd

# Load performance data
performance = pd.read_csv("data/processed/07_scheme_performance_cleaned.csv")

def recommend_funds(risk):
    risk = risk.capitalize()

    funds = performance[
        performance["risk_grade"].str.capitalize() == risk
    ]

    funds = funds.sort_values(
        by="sharpe_ratio",
        ascending=False
    )

    print("\nTop 3 Recommended Funds\n")
    print(
        funds[
            [
                "scheme_name",
                "fund_house",
                "category",
                "risk_grade",
                "sharpe_ratio"
            ]
        ].head(3)
    )

risk = input("Enter Risk Appetite (Low / Moderate / High): ")
recommend_funds(risk)
