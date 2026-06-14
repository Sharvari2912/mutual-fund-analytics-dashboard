# Data Dictionary

## 01_fund_master

| Column | Data Type | Definition |
|----------|-----------|-------------|
| amfi_code | Integer | Unique AMFI scheme code |
| fund_house | Text | Name of Asset Management Company |
| scheme_name | Text | Name of the mutual fund scheme |
| category | Text | Broad scheme category (Equity, Debt, etc.) |
| sub_category | Text | Scheme sub-category (Large Cap, Mid Cap, etc.) |
| plan | Text | Direct or Regular plan |
| launch_date | Date | Scheme launch date |
| benchmark | Text | Benchmark index of the scheme |
| expense_ratio_pct | Float | Expense ratio percentage |
| exit_load_pct | Float | Exit load percentage |
| min_sip_amount | Integer | Minimum SIP investment amount |
| min_lumpsum_amount | Integer | Minimum lumpsum investment amount |
| fund_manager | Text | Fund manager name |
| risk_category | Text | Risk level of the scheme |
| sebi_category_code | Text | SEBI classification code |

Source: AMFI / Mutual Fund Master Data

---

## 02_nav_history

| Column | Data Type | Definition |
|----------|-----------|-------------|
| amfi_code | Integer | AMFI scheme code |
| date | Date | NAV date |
| nav | Float | Net Asset Value of the scheme |

Source: MFAPI Historical NAV Data

---

## 03_aum_by_fund_house

| Column | Data Type | Definition |
|----------|-----------|-------------|
| fund_house | Text | Mutual fund company |
| month | Date/Text | Reporting month |
| aum_crore | Float | Assets Under Management (₹ Crore) |

Source: AMFI

---

## 04_monthly_sip_inflows

| Column | Data Type | Definition |
|----------|-----------|-------------|
| month | Date/Text | Reporting month |
| sip_inflow_crore | Float | Monthly SIP inflow amount (₹ Crore) |

Source: AMFI

---

## 05_category_inflows

| Column | Data Type | Definition |
|----------|-----------|-------------|
| category | Text | Mutual fund category |
| month | Date/Text | Reporting month |
| inflow_crore | Float | Net inflow/outflow amount (₹ Crore) |

Source: AMFI

---

## 06_industry_folio_count

| Column | Data Type | Definition |
|----------|-----------|-------------|
| month | Date/Text | Reporting month |
| folio_count | Integer | Number of investor folios |

Source: AMFI

---

## 07_scheme_performance

| Column | Data Type | Definition |
|----------|-----------|-------------|
| amfi_code | Integer | AMFI scheme code |
| scheme_name | Text | Mutual fund scheme name |
| fund_house | Text | Asset management company |
| category | Text | Scheme category |
| plan | Text | Direct or Regular plan |
| return_1yr_pct | Float | 1-year return (%) |
| return_3yr_pct | Float | 3-year return (%) |
| return_5yr_pct | Float | 5-year return (%) |
| benchmark_3yr_pct | Float | 3-year benchmark return (%) |
| alpha | Float | Risk-adjusted excess return |
| beta | Float | Volatility relative to benchmark |
| sharpe_ratio | Float | Risk-adjusted return measure |
| sortino_ratio | Float | Downside risk-adjusted return |
| std_dev_ann_pct | Float | Annualized standard deviation (%) |
| max_drawdown_pct | Float | Maximum decline from peak (%) |
| aum_crore | Float | Assets Under Management (₹ Crore) |
| expense_ratio_pct | Float | Expense ratio (%) |
| morningstar_rating | Integer | Morningstar rating (1–5) |
| risk_grade | Text | Risk category |

Source: Scheme Performance Dataset

---

## 08_investor_transactions

| Column | Data Type | Definition |
|----------|-----------|-------------|
| transaction_id | Integer | Unique transaction identifier |
| investor_id | Integer | Unique investor identifier |
| amfi_code | Integer | AMFI scheme code |
| transaction_date | Date | Date of transaction |
| transaction_type | Text | SIP, Lumpsum, or Redemption |
| amount | Float | Transaction amount |
| state | Text | Investor state |
| kyc_status | Text | Investor KYC verification status |

Source: Investor Transaction Dataset

---

## 09_portfolio_holdings

| Column | Data Type | Definition |
|----------|-----------|-------------|
| amfi_code | Integer | AMFI scheme code |
| holding_name | Text | Security/company name |
| sector | Text | Industry sector |
| asset_type | Text | Equity, Debt, Cash, etc. |
| allocation_pct | Float | Portfolio allocation percentage |

Source: Portfolio Holdings Dataset

---

## 10_benchmark_indices

| Column | Data Type | Definition |
|----------|-----------|-------------|
| benchmark_name | Text | Benchmark index name |
| date | Date | Observation date |
| index_value | Float | Benchmark index value |

Source: Benchmark Index Dataset