# Mutual Fund Analytics - Data Dictionary

## Overview

This document describes the datasets, tables, columns, data types, and business definitions used in the Mutual Fund Analytics project.

---

## Table: dim_fund

| Column Name   | Data Type | Description                |
| ------------- | --------- | -------------------------- |
| amfi_code     | INTEGER   | Unique AMFI scheme code    |
| fund_house    | TEXT      | Mutual fund company (AMC)  |
| scheme_name   | TEXT      | Name of mutual fund scheme |
| category      | TEXT      | Fund category              |
| sub_category  | TEXT      | Fund sub-category          |
| plan          | TEXT      | Direct or Regular plan     |
| risk_category | TEXT      | Risk classification        |

---

## Table: fact_nav

| Column Name | Data Type | Description      |
| ----------- | --------- | ---------------- |
| amfi_code   | INTEGER   | AMFI scheme code |
| date        | DATE      | NAV date         |
| nav         | REAL      | Net Asset Value  |

---

## Table: fact_transactions

| Column Name        | Data Type | Description                |
| ------------------ | --------- | -------------------------- |
| investor_id        | TEXT      | Unique investor identifier |
| transaction_date   | DATE      | Transaction date           |
| amfi_code          | INTEGER   | AMFI scheme code           |
| transaction_type   | TEXT      | SIP, Lumpsum, Redemption   |
| amount_inr         | REAL      | Transaction amount in INR  |
| state              | TEXT      | Investor state             |
| city               | TEXT      | Investor city              |
| city_tier          | TEXT      | Tier classification        |
| age_group          | TEXT      | Investor age group         |
| gender             | TEXT      | Investor gender            |
| annual_income_lakh | REAL      | Annual income in lakhs     |
| payment_mode       | TEXT      | Payment method             |
| kyc_status         | TEXT      | KYC verification status    |

---

## Table: fact_performance

| Column Name       | Data Type | Description              |
| ----------------- | --------- | ------------------------ |
| amfi_code         | INTEGER   | AMFI scheme code         |
| return_1yr_pct    | REAL      | 1-Year return percentage |
| return_3yr_pct    | REAL      | 3-Year return percentage |
| return_5yr_pct    | REAL      | 5-Year return percentage |
| alpha             | REAL      | Alpha metric             |
| beta              | REAL      | Beta metric              |
| sharpe_ratio      | REAL      | Sharpe ratio             |
| sortino_ratio     | REAL      | Sortino ratio            |
| max_drawdown_pct  | REAL      | Maximum drawdown         |
| expense_ratio_pct | REAL      | Expense ratio percentage |
| risk_grade        | TEXT      | Risk grade               |

---

## Table: fact_aum

| Column Name    | Data Type | Description                          |
| -------------- | --------- | ------------------------------------ |
| date           | DATE      | AUM reporting date                   |
| fund_house     | TEXT      | Mutual fund company                  |
| aum_lakh_crore | REAL      | Assets under management (Lakh Crore) |
| aum_crore      | REAL      | Assets under management (Crore)      |
| num_schemes    | INTEGER   | Number of schemes                    |

---

## Data Sources

1. Fund Master Dataset
2. NAV History Dataset
3. AUM by Fund House Dataset
4. Monthly SIP Inflows Dataset
5. Category Inflows Dataset
6. Industry Folio Count Dataset
7. Scheme Performance Dataset
8. Investor Transactions Dataset
9. Portfolio Holdings Dataset
10. Benchmark Indices Dataset

---

## Project

Mutual Fund Analytics Capstone Project

Database: SQLite

Database File: bluestock_mf.db
