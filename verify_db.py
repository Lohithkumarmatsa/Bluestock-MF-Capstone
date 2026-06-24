import sqlite3

conn = sqlite3.connect("bluestock_mf.db")

cursor = conn.cursor()

tables = [
    "fund_master",
    "nav_history",
    "scheme_performance",
    "investor_transactions"
]

for table in tables:
    cursor.execute(f"SELECT COUNT(*) FROM {table}")
    count = cursor.fetchone()[0]
    print(f"{table}: {count} rows")

conn.close()