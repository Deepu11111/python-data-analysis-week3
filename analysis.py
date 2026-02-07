import pandas as pd
# 1. Load DataSet
df = pd.read_csv("data/students.csv")
df["marks"]=pd.to_numeric(df["marks"],errors="coerce")

# 2.Show First rows
print("First 5 rows:")
print(df.head())

#3.Basic Information 
print("\nShape (rows,columns):",df.shape)
print("\nData types:")
print(df.info())

#4.Misssing Values
print("\nMissing values count:")
print(df.isnull().sum())

#5. Fill missing values
df["marks"] = df["marks"].fillna(df["marks"].mean())
df["age"] = df["age"].fillna(0)

print("\nAfter cleaning:")
print(df)

#6. Statistics
print("\nAverage Marks:",df["marks"].mean())
print("\nHighest Marks:",df["marks"].max())
print("\nLowest Marks:",df["marks"].min())
