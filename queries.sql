-- 1 Top 5 Funds by AUM
SELECT scheme_name, aum_crore
FROM scheme_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2 Average NAV
SELECT AVG(nav)
FROM nav_history;

-- 3 Average NAV by AMFI Code
SELECT amfi_code, AVG(nav)
FROM nav_history
GROUP BY amfi_code;

-- 4 Expense Ratio below 1%
SELECT scheme_name, expense_ratio_pct
FROM scheme_performance
WHERE expense_ratio_pct < 1;

-- 5 Transactions by State
SELECT state, COUNT(*)
FROM investor_transactions
GROUP BY state;

-- 6 SIP Transactions Count
SELECT COUNT(*)
FROM investor_transactions
WHERE transaction_type='SIP';

-- 7 Redemption Transactions Count
SELECT COUNT(*)
FROM investor_transactions
WHERE transaction_type='Redemption';

-- 8 Fund Count by Category
SELECT category, COUNT(*)
FROM fund_master
GROUP BY category;

-- 9 Average 1 Year Return
SELECT AVG(return_1yr_pct)
FROM scheme_performance;

-- 10 Top 5 Performing Funds
SELECT scheme_name, return_5yr_pct
FROM scheme_performance
ORDER BY return_5yr_pct DESC
LIMIT 5;