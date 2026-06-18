import pandas as pd
import numpy as np

# Read CSV
df = pd.read_csv("sales.csv")

print("Original Dataset")
print(df)

# Remove missing values
df.dropna(inplace=True)

# Correct Data Types
df["quantity"] = df["quantity"].astype(int)
df["price"] = df["price"].astype(float)
df["cost"] = df["cost"].astype(float)

# Revenue
df["revenue"] = df["quantity"] * df["price"]

# Profit
df["profit"] = df["revenue"] - (df["quantity"] * df["cost"])

# Discount Percentage
df["discount_percentage"] = np.random.randint(
    5,
    20,
    size=len(df)
)

# Profit Margin
df["profit_margin"] = (
    df["profit"] /
    df["revenue"]
) * 100

# Save Cleaned Dataset
df.to_csv(
    "cleaned_sales.csv",
    index=False
)

print("\nCleaned Dataset")
print(df)

# Revenue By Product
product_summary = df.groupby(
    "product_name"
)[["revenue","profit"]].sum()

print("\nRevenue By Product")
print(product_summary)

# Revenue By Store
store_summary = df.groupby(
    "store_id"
)[["revenue","profit"]].sum()

print("\nRevenue By Store")
print(store_summary)

# Top Product
top_product = product_summary.sort_values(
    by="revenue",
    ascending=False
)

print("\nTop Selling Products")
print(top_product)

# Underperforming Products
bottom_product = product_summary.sort_values(
    by="revenue"
)

print("\nUnderperforming Products")
print(bottom_product)
