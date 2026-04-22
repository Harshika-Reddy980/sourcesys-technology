import matplotlib.pyplot as plt
import numpy as np

# -------------------------------
# Line Graph
# -------------------------------

months = ["Jan","Feb","Mar","Apr","May"]
sales = [200,300,400,350,500]

plt.figure(figsize=(6,4))
plt.plot(months, sales, marker='o')
plt.title("Monthly Sales Growth")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.grid(True)
plt.show()


# -------------------------------
# Bar Chart
# -------------------------------

products = ["Laptop","Mobile","Tablet","Headphones"]
revenue = [50000,70000,20000,15000]

plt.figure(figsize=(6,4))
plt.bar(products, revenue)
plt.title("Product Revenue Comparison")
plt.xlabel("Products")
plt.ylabel("Revenue")
plt.show()


# -------------------------------
# Pie Chart
# -------------------------------

labels = ["Python","Java","C++","JavaScript"]
sizes = [40,25,20,15]

plt.figure(figsize=(6,4))
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Programming Language Popularity")
plt.show()


# -------------------------------
# Scatter Plot
# -------------------------------

study_hours = [1,2,3,4,5,6,7,8]
scores = [35,40,50,55,60,65,70,80]

plt.figure(figsize=(6,4))
plt.scatter(study_hours, scores)
plt.title("Study Hours vs Exam Score")
plt.xlabel("Study Hours")
plt.ylabel("Score")
plt.show()


# -------------------------------
# Histogram
# -------------------------------

data = np.random.normal(60,10,100)

plt.figure(figsize=(6,4))
plt.hist(data, bins=10)
plt.title("Distribution of Exam Scores")
plt.xlabel("Scores")
plt.ylabel("Frequency")
plt.show()