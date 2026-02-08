import pandas as pd

#1.Load CSV File

df = pd.read_csv("sales_data.csv")


#2.Show first few rows

print("First 5 rows:")
print(df.head())

#3.Explore Data
print("\nShape (rows,columns):")
print(df.shape)

print("\nColumn names:")
print(df.columns)

print("\nData types and info:")
print(df.info())

print("\nBasic statistics:")
print(df.describe())

#4.Data Cleaning
print("\n--- Checking missing values-----")
print(df.isnull().sum())

print("\n---Removing Duplicates---")
print(df.drop_duplicates())

# Convert numeric colmn to propr type
df["Quantity"] = pd.to_numeric(df["Quantity"],errors="coerce")
df["Price"] = pd.to_numeric(df["Price"],errors="coerce")
df["Total_Sales"] = pd.to_numeric(df["Total_Sales"],errors="coerce")

#fill missing numeric values with 0
df["Quantity"] = df["Quantity"].fillna(0)
df["Price"] = df["Price"].fillna(0)
df["Total_Sales"]=df["Total_Sales"].fillna(0)

print("\n--after cleaning--")
print(df.info())

#5. Sales Analysis

print("---SALES ANALYSIS---")
#a.Total revenue
total_revenue = df["Quantity"].sum()
print(f"\nTotal Revenue:Rs{total_revenue:,.2f}")

#b.Total Quantity Sold
total_quty = df["Quantity"].sum()
print(f"Total Quantity Sold:{int(total_quty)}")

#c.Best Selling Product(by revenue)
best_product  =df.groupby("Product")["Total_Sales"].sum().sort_values(ascending=False)
print("\nRevenue by product:")
print(best_product)
print(f"\nBest Selling Product (Revenue):{best_product.idxmax()}")

#d.Region wise sales
region_sales = df.groupby("Region")["Total_Sales"].sum()
print("\nRegion-wise Sales:")
print(region_sales)

#e. Highest single order
max_order = df["Total_Sales"].max()
print(f"\nHighest Single Order Value:Rs{max_order:,.2f}")
