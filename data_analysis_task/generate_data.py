import pandas as pd
import numpy as np

np.random.seed(42)

months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct"]
products = ["Laptop","Mobile","Tablet","Headphones","Camera"]

data = []

for i in range(100):
    month = np.random.choice(months)
    product = np.random.choice(products)
    sales = np.random.randint(10000,80000)

    data.append([month, product, sales])

df = pd.DataFrame(data, columns=["Month","Product","Sales"])

df.to_csv("sales_data.csv", index=False)

print("Dataset with 100 entries created successfully!")