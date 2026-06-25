-- 1. Top 5 Funds by AUM
SELECT fund_house,
       MAX(aum_crore) AS max_aum
FROM fact_aum
GROUP BY fund_house
ORDER BY max_aum DESC
LIMIT 5;

-- 2. Average NAV per Fund
SELECT amfi_code,
       AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY amfi_code;

-- 3. Transactions by State
SELECT state,
       COUNT(*) AS total_transactions,
       SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_amount DESC;

-- 4. Funds with Expense Ratio < 1%
SELECT amfi_code,
       expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 5. Top 5 Funds by 5Y Return
SELECT amfi_code,
       return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 5;

-- 6. Average 1Y Return by Category
SELECT category,
       AVG(return_1yr_pct) AS avg_return
FROM fact_performance fp
JOIN dim_fund df
ON fp.amfi_code = df.amfi_code
GROUP BY category;

-- 7. Fund Count by Risk Category
SELECT risk_category,
       COUNT(*) AS total_funds
FROM dim_fund
GROUP BY risk_category;

-- 8. Top Cities by Investment Amount
SELECT city,
       SUM(amount_inr) AS total_investment
FROM fact_transactions
GROUP BY city
ORDER BY total_investment DESC
LIMIT 10;

-- 9. Monthly Average NAV
SELECT substr(nav_date,1,7) AS month,
       AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY month
ORDER BY month;

-- 10. Transaction Type Distribution
SELECT transaction_type,
       COUNT(*) AS total
FROM fact_transactions
GROUP BY transaction_type;