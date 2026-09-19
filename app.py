import streamlit as st
import pandas as pd


# =========================
# PAGE CONFIGURATION
# =========================

st.set_page_config(
    page_title="Supermarket Sales Dashboard",
    page_icon="📊",
    layout="wide"
)


# =========================
# LOAD DATA
# =========================

df = pd.read_csv("sales_data.csv")

df["Date"] = pd.to_datetime(df["Date"])


# =========================
# SIDEBAR FILTERS
# =========================

st.sidebar.title("🎛️ Filters")

# Product Category
categories = sorted(df["Product_Category"].unique())

selected_category = st.sidebar.multiselect(
    "Product Category",
    categories,
    default=categories
)

# Payment Method
payments = sorted(df["Payment_Method"].unique())

selected_payment = st.sidebar.multiselect(
    "Payment Method",
    payments,
    default=payments
)

# Customer Type
customers = sorted(df["Customer_Type"].unique())

selected_customer = st.sidebar.multiselect(
    "Customer Type",
    customers,
    default=customers
)


# =========================
# APPLY FILTERS
# =========================

filtered_df = df[
    (df["Product_Category"].isin(selected_category))
    & (df["Payment_Method"].isin(selected_payment))
    & (df["Customer_Type"].isin(selected_customer))
]


# =========================
# TITLE
# =========================

st.title("📊 Supermarket Sales Dashboard")

st.write(
    "Interactive sales analysis dashboard for supermarket transactions."
)


# =========================
# KPI CALCULATIONS
# =========================

total_sales = filtered_df["Net_Sales"].sum()

average_order_value = (
    filtered_df["Net_Sales"].mean()
    if len(filtered_df) > 0
    else 0
)

total_quantity = filtered_df["Quantity"].sum()

total_discount = filtered_df["Discount_Amount"].sum()


# =========================
# KPI CARDS
# =========================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "💰 Total Sales",
        f"₹{total_sales:,.0f}"
    )

with col2:
    st.metric(
        "🛒 Average Order Value",
        f"₹{average_order_value:,.2f}"
    )

with col3:
    st.metric(
        "📦 Quantity Sold",
        f"{total_quantity:,}"
    )

with col4:
    st.metric(
        "💸 Discount Given",
        f"₹{total_discount:,.0f}"
    )


st.divider()


# =========================
# SALES BY CATEGORY
# =========================

st.subheader("📊 Sales by Product Category")

category_sales = (
    filtered_df.groupby("Product_Category")["Net_Sales"]
    .sum()
    .sort_values(ascending=False)
)

st.bar_chart(category_sales)


# =========================
# SALES BY PAYMENT METHOD
# =========================

st.subheader("💳 Sales by Payment Method")

payment_sales = (
    filtered_df.groupby("Payment_Method")["Net_Sales"]
    .sum()
    .sort_values(ascending=False)
)

st.bar_chart(payment_sales)


# =========================
# SALES BY CUSTOMER TYPE
# =========================

st.subheader("👥 Sales by Customer Type")

customer_sales = (
    filtered_df.groupby("Customer_Type")["Net_Sales"]
    .sum()
    .sort_values(ascending=False)
)

st.bar_chart(customer_sales)


# =========================
# MONTHLY SALES TREND
# =========================

st.subheader("📈 Monthly Sales Trend")

monthly_sales = (
    filtered_df.groupby(
        filtered_df["Date"].dt.to_period("M")
    )["Net_Sales"]
    .sum()
)

monthly_sales.index = monthly_sales.index.to_timestamp()

st.line_chart(monthly_sales)


# =========================
# DATA SUMMARY
# =========================

st.divider()

st.subheader("📋 Filtered Transaction Data")

st.write(
    f"Showing **{len(filtered_df):,} transactions**"
)

st.dataframe(
    filtered_df,
    use_container_width=True
)

# =========================
# BUSINESS INSIGHTS
# =========================

st.divider()

st.subheader("💡 Business Insights")

if len(filtered_df) > 0:

    # Top product category
    top_category = (
        filtered_df.groupby("Product_Category")["Net_Sales"]
        .sum()
        .idxmax()
    )

    top_category_sales = (
        filtered_df.groupby("Product_Category")["Net_Sales"]
        .sum()
        .max()
    )

    # Top payment method
    top_payment = (
        filtered_df.groupby("Payment_Method")["Net_Sales"]
        .sum()
        .idxmax()
    )

    # Top customer type
    top_customer = (
        filtered_df.groupby("Customer_Type")["Net_Sales"]
        .sum()
        .idxmax()
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info(
            f"🏆 **Top Category**\n\n"
            f"{top_category}\n\n"
            f"Sales: ₹{top_category_sales:,.0f}"
        )

    with col2:
        st.info(
            f"💳 **Top Payment Method**\n\n"
            f"{top_payment}"
        )

    with col3:
        st.info(
            f"👥 **Top Customer Segment**\n\n"
            f"{top_customer}"
        )

else:

    st.warning(
        "No transactions match the selected filters."
    )

    # =========================
# DOWNLOAD FILTERED DATA
# =========================

st.divider()

st.subheader("⬇️ Download Data")

csv_data = filtered_df.to_csv(index=False)

st.download_button(
    label="📥 Download Filtered CSV",
    data=csv_data,
    file_name="filtered_supermarket_sales.csv",
    mime="text/csv"
)