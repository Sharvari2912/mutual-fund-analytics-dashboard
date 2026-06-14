-- Top 5 fund houses by AUM
SELECT * FROM aum_by_fund_house
ORDER BY aum_crore DESC
LIMIT 5;

-- Average NAV by scheme
SELECT amfi_code, AVG(nav)
FROM nav_history
GROUP BY amfi_code;

-- Monthly SIP inflows
SELECT * FROM monthly_sip_inflows;

-- Category inflows
SELECT * FROM category_inflows;

-- Industry folio count
SELECT * FROM industry_folio_count;

-- Funds with expense ratio below 1%
SELECT scheme_name, expense_ratio_pct
FROM scheme_performance
WHERE expense_ratio_pct < 1;

-- Top 5 schemes by 5-year return
SELECT scheme_name, return_5yr_pct
FROM scheme_performance
ORDER BY return_5yr_pct DESC
LIMIT 5;

-- Morningstar 5-star funds
SELECT scheme_name
FROM scheme_performance
WHERE morningstar_rating = 5;

-- Count of schemes by category
SELECT category, COUNT(*)
FROM fund_master
GROUP BY category;

-- Highest NAV recorded per scheme
SELECT amfi_code, MAX(nav)
FROM nav_history
GROUP BY amfi_code;