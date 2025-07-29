import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load dataset
df = pd.read_csv("sales_data.csv")  # Replace with your actual dataset filename

# Display first few rows
print(df.head())

# Step 2: Line plot for month-wise profit
plt.figure(figsize=(10, 5))
plt.plot(df['Month'], df['Total Profit'], linestyle='dotted', marker='o', color='red', linewidth=3, label='Profit')
plt.title('Month-wise Profit')
plt.xlabel('Month')
plt.ylabel('Profit')
plt.legend()
plt.grid(True)
plt.show()

# Step 3: Multi-line plot of sales for all products
plt.figure(figsize=(10, 6))
plt.plot(df['Month'], df['Face Cream'], marker='o', label='Face Cream')
plt.plot(df['Month'], df['Face Wash'], marker='s', label='Face Wash')
plt.plot(df['Month'], df['Toothpaste'], marker='^', label='Toothpaste')
plt.plot(df['Month'], df['Shampoo'], marker='*', label='Shampoo')
plt.plot(df['Month'], df['Moisturizer'], marker='D', label='Moisturizer')
plt.title('Monthly Product Sales')
plt.xlabel('Month')
plt.ylabel('Units Sold')
plt.legend()
plt.grid(True)
plt.show()

# Step 4: Bar plot comparing face cream and face wash sales
import numpy as np

months = df['Month']
x = np.arange(len(months))
width = 0.35

plt.figure(figsize=(10, 5))
plt.bar(x - width/2, df['Face Cream'], width=width, label='Face Cream')
plt.bar(x + width/2, df['Face Wash'], width=width, label='Face Wash')
plt.xticks(x, months, rotation=45)
plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Face Cream vs Face Wash Sales per Month')
plt.legend()
plt.tight_layout()
plt.show()
