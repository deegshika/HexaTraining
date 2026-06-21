import pandas as pd
import numpy as np

np.random.seed(42)

num_rows = 5000

store_ids = [101, 102, 103, 104, 105]
store_names = {
    101: "Chennai Store",
    102: "Bangalore Store",
    103: "Hyderabad Store",
    104: "Mumbai Store",
    105: "Delhi Store"
}

product_ids = [201, 202, 203, 204, 205, 206, 207, 208]
product_names = {
    201: "Laptop",
    202: "Mobile",
    203: "Headphones",
    204: "Keyboard",
    205: "Mouse",
    206: "Monitor",
    207: "Tablet",
    208: "Printer"
}

dates = pd.date_range(start="2026-01-01", end="2026-06-30", freq="D")

data = []

for i in range(1, num_rows + 1):
    store_id = np.random.choice(store_ids)
    product_id = np.random.choice(product_ids)

    quantity = np.random.randint(1, 8)
    price = np.random.randint(500, 60000)
    cost = int(price * np.random.uniform(0.6, 0.9))
    returns = np.random.randint(0, 4)

    sale_date = np.random.choice(dates)

    data.append([
        i,
        store_id,
        store_names[store_id],
        product_id,
        product_names[product_id],
        quantity,
        price,
        cost,
        returns,
        sale_date
    ])

df = pd.DataFrame(data, columns=[
    "sale_id",
    "store_id",
    "store_name",
    "product_id",
    "product_name",
    "quantity",
    "price",
    "cost",
    "returns",
    "sale_date"
])

df.to_csv("large_sales.csv", index=False)

print("large_sales.csv created successfully with", len(df), "rows")
print(df.head())
