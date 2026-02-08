import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel(r"C:\Users\abhin\OneDrive\Desktop\INT217\Coffee Shop Sales.xlsx")

print(df.head(10))

# Objective 1 : Summary of data & checking for null values
print("\nSummary statistics : ")
print(df.info())
print(df.describe())

print("\nMissing Values in Each Column:")
print(df.isnull().sum())

# Objective 2 : Calculate total sales revenue 
print("\n Total Sales revenue: ")
df['total_revenue'] = df['transaction_qty'] * df['unit_price']

total_revenue = df['total_revenue'].sum()
print(total_revenue)


# Objective 3: Top 10 Most Sold Products (by quantity) & Bar Chart
print("\nTop 10 Most Sold Products (by quantity): ")
top_products = df.groupby('product_detail')['transaction_qty'].sum().sort_values(ascending=False).head(10)
print(top_products)

plt.figure(figsize=(10, 6))
sns.barplot(x=top_products.values, y=top_products.index, hue=top_products.index, palette='magma')
plt.title("Top 10 Most Sold Products")
plt.xlabel("Total Quantity Sold")
plt.ylabel("Product Detail")
plt.tight_layout()
plt.show()


#Objective 4: Sales by Store Location & Bar Chart
# Total revenue by store location
store_sales = df.groupby('store_location')['total_revenue'].sum().sort_values(ascending=False)
print("\nSales by store: \n", store_sales)
plt.figure(figsize=(10, 6))
sns.barplot(x=store_sales.values, y=store_sales.index, hue=store_sales.index, palette='viridis')
plt.title("Total Sales by Store Location")
plt.xlabel("Total Sales Revenue ($)")
plt.ylabel("Store Location")
plt.tight_layout()
plt.show()

#Pie Chart for total revenue by Store Location
plt.figure(figsize=(8, 8))
plt.pie(store_sales, labels=store_sales.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
plt.title('Sales Revenue Distribution by Store Location')
plt.axis('equal')  
plt.tight_layout()
plt.show()


#Objective 5: Compute correlation matrix & Heatmap
corr = df.corr(numeric_only=True)

plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, fmt=".2f", cmap='coolwarm', linewidths=0.5, square=True)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

#Objective 6: Sales trend over time & it's Line Chart
df['transaction_date'] = pd.to_datetime(df['transaction_date'])
daily_sales = df.groupby('transaction_date')['total_revenue'].sum().reset_index()

plt.figure(figsize=(12, 6))
sns.lineplot(x='transaction_date', y='total_revenue', data=daily_sales, marker='o', color='teal')
plt.title('Daily Sales Trend')
plt.xlabel('Date')
plt.ylabel('Total Revenue ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

