# 📊 Supermarket Sales Analysis & Interactive Dashboard
## 🚀 Live Demo

👉 [Open the Interactive Supermarket Sales Dashboard](https://supermarket-sales-analysis-nctatywenzqb8aubg55f48.streamlit.app/)

The dashboard provides interactive filters, sales KPIs, category analysis, payment-method analysis, customer-segment analysis, monthly trends, and downloadable filtered data.

## 📌 Project Overview

This project analyzes supermarket transaction data using Python and
presents the results through an interactive Streamlit dashboard.

The goal is to transform raw sales data into meaningful business insights
that can help understand sales performance, customer behavior, payment
preferences, and sales trends.

---

## 🎯 Business Questions

This project answers questions such as:

- How much total revenue was generated?
- What is the average order value?
- Which product category generates the highest sales?
- Which payment method contributes the most sales?
- Do regular or new customers generate more revenue?
- How do sales change over time?
- Can users filter the analysis and export the filtered data?

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Streamlit
- PowerShell
- VS Code

---

## 📂 Dataset

The dataset contains 5,000 supermarket transactions.

### Columns

| Column | Description |
|---|---|
| Date | Transaction date and time |
| Product_Category | Product category |
| Payment_Method | Payment method |
| Customer_Type | New or regular customer |
| Quantity | Number of products purchased |
| Unit_Price | Price per product |
| Discount | Discount percentage |
| Gross_Sales | Sales before discount |
| Discount_Amount | Discount value |
| Net_Sales | Final sales after discount |

---

## 📊 Key Results

### Dataset

- Transactions: 5,000
- Columns: 10
- Missing values: 0

### Sales Performance

- Total Sales: ₹22,009,741.76
- Average Order Value: ₹4,401.95
- Total Quantity Sold: 20,038
- Total Discount Given: ₹3,990,794.42

### Top Category

Electronics generated the highest total sales.

### Payment Method

Debit Card generated the highest sales among the available payment methods.

### Customer Segment

Regular customers generated more total sales than new customers in this dataset.

---

## 📈 Dashboard Features

The Streamlit dashboard provides:

- KPI cards
- Product category analysis
- Payment method analysis
- Customer type analysis
- Monthly sales trend
- Interactive filters
- Automatic business insights
- Filtered transaction table
- CSV download

---

## 🖥️ Running the Dashboard Locally

### 1. Install dependencies

```bash
pip install pandas numpy matplotlib streamlit