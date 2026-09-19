import pandas as pd

# Load the dataset
df = pd.read_csv(
    r"C:\Users\Zoho\Desktop\Online-Earning-2026\02_Portfolio\Supermarket-Sales-Analysis\sales_data.csv"
)
# Show basic information
print("========== DATASET SHAPE ==========")
print(df.shape)

print("\n========== COLUMN NAMES ==========")
print(df.columns.tolist())

print("\n========== FIRST 5 ROWS ==========")
print(df.head())

print("\n========== DATA TYPES ==========")
print(df.dtypes)

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

print("\n========== BASIC STATISTICS ==========")
print(df.describe())

print("\n========== BUSINESS KPIs ==========")

total_sales = df["Net_Sales"].sum()
average_order_value = df["Net_Sales"].mean()
total_quantity = df["Quantity"].sum()
total_discount = df["Discount_Amount"].sum()

print(f"Total Sales: ₹{total_sales:,.2f}")
print(f"Average Order Value: ₹{average_order_value:,.2f}")
print(f"Total Quantity Sold: {total_quantity:,}")
print(f"Total Discount Given: ₹{total_discount:,.2f}")


print("\n========== SALES BY PRODUCT CATEGORY ==========")

category_sales = (
    df.groupby("Product_Category")["Net_Sales"]
    .sum()
    .sort_values(ascending=False)
)

print(category_sales)


print("\n========== SALES BY PAYMENT METHOD ==========")

payment_sales = (
    df.groupby("Payment_Method")["Net_Sales"]
    .sum()
    .sort_values(ascending=False)
)

print(payment_sales)


print("\n========== SALES BY CUSTOMER TYPE ==========")

customer_sales = (
    df.groupby("Customer_Type")["Net_Sales"]
    .sum()
    .sort_values(ascending=False)
)

print(customer_sales)

import matplotlib.pyplot as plt


print("\n========== CREATING CATEGORY SALES CHART ==========")

plt.figure(figsize=(10, 6))

category_sales.sort_values().plot(
    kind="barh"
)

plt.title("Sales by Product Category")
plt.xlabel("Net Sales (₹)")
plt.ylabel("Product Category")

plt.tight_layout()

plt.savefig(
    "reports/category_sales.png",
    dpi=300
)

plt.show()

print("Chart saved successfully!")

print("\n========== CREATING PAYMENT METHOD CHART ==========")

plt.figure(figsize=(9, 6))

payment_sales.sort_values().plot(
    kind="barh"
)

plt.title("Sales by Payment Method")
plt.xlabel("Net Sales (₹)")
plt.ylabel("Payment Method")

plt.tight_layout()

plt.savefig(
    "reports/payment_method_sales.png",
    dpi=300
)

plt.show()

print("Payment method chart saved successfully!")

print("\n========== CREATING CUSTOMER TYPE CHART ==========")

plt.figure(figsize=(8, 6))

customer_sales.sort_values().plot(
    kind="barh"
)

plt.title("Sales by Customer Type")
plt.xlabel("Net Sales (₹)")
plt.ylabel("Customer Type")

plt.tight_layout()

plt.savefig(
    "reports/customer_type_sales.png",
    dpi=300
)

plt.show()

print("Customer type chart saved successfully!")

print("\n========== CREATING MONTHLY SALES TREND ==========")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Calculate monthly sales
monthly_sales = (
    df.groupby(df["Date"].dt.to_period("M"))["Net_Sales"]
    .sum()
)

# Convert period to timestamp for plotting
monthly_sales.index = monthly_sales.index.to_timestamp()

plt.figure(figsize=(12, 6))

plt.plot(
    monthly_sales.index,
    monthly_sales.values,
    marker="o"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Net Sales (₹)")
plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    "reports/monthly_sales_trend.png",
    dpi=300
)

plt.show()

print("Monthly sales trend saved successfully!")
