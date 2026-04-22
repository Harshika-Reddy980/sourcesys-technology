import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("C:\\Users\\91630\\OneDrive\\Desktop\\Sourcesys_technology\\sales_data.csv")

print("Dataset Preview")
print(data.head())

# Basic analysis
total_sales = np.sum(data["Sales"])
average_sales = np.mean(data["Sales"])

print("\nTotal Sales:", total_sales)
print("Average Sales:", average_sales)

# Sales by product
product_sales = data.groupby("Product")["Sales"].sum()

print("\nSales by Product")
print(product_sales)

# Monthly sales
monthly_sales = data.groupby("Month")["Sales"].sum()

# Graph 1 - Line
plt.plot(monthly_sales.index, monthly_sales.values, marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

# Graph 2 - Bar
product_sales.plot(kind='bar')
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.show()

# Graph 3 - Pie
plt.pie(product_sales.values, labels=product_sales.index, autopct='%1.1f%%')
plt.title("Sales Distribution by Product")
plt.show()

# Graph 4 - Histogram
plt.hist(data["Sales"], bins=10)
plt.title("Sales Frequency Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.show()

# Graph 5 - Scatter
plt.scatter(data.index, data["Sales"])
plt.title("Sales Scatter Plot")
plt.xlabel("Transaction")
plt.ylabel("Sales")
plt.show()