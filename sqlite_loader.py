import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///bluestock_mf.db")

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")
scheme_perf = pd.read_csv("data/raw/07_scheme_performance.csv")
transactions = pd.read_csv("data/raw/08_investor_transactions.csv")

fund_master.to_sql("fund_master", engine, if_exists="replace", index=False)
nav_history.to_sql("nav_history", engine, if_exists="replace", index=False)
scheme_perf.to_sql("scheme_performance", engine, if_exists="replace", index=False)
transactions.to_sql("investor_transactions", engine, if_exists="replace", index=False)

print("Database created successfully!")