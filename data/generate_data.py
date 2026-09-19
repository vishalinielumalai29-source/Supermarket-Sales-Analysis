import pandas as pd 
import numpy as np 

np.random.seed(42)

n = 5000

data = {
    "Date": pd.date_range("2025-01-01", periods=n, freq="6h"),
    "Product_Category": np.random.choice(
        ["Electronics", "Groceries", "Clothing", "Home & Kitchen", "Beauty"],
        n
    ),
    "Payment_Method": np.random.choice(
        ["UPI", "Credit Card", "Debit Card", "Cash"],
        n
    ),
    "Customer_Type": np.random.choice(
        ["Regular", "New"],
        n,
        p=[0.65, 0.35]
    ),
    "Quantity": np.random.randint(1, 8, n),
    "Unit_Price": np.round(np.random.uniform(50, 2500, n), 2),
    "Discount": np.round(np.random.uniform(0, 0.30, n), 2)
}

df = pd.DataFrame(data)

df["Gross_Sales"] = df["Quantity"] * df["Unit_Price"]

df["Discount_Amount"] = (
    df["Gross_Sales"] * df["Discount"]
)

df["Net_Sales"] = (
    df["Gross_Sales"] - df["Discount_Amount"]
)

df.to_csv("sales_data.csv", index=False)

print("Dataset created successfully!")
print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")
print(df.head())

