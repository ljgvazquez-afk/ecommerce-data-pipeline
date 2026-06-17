import pandas as pd

df = pd.read_csv("data/raw/products.csv")

df["price"] = df["price"].astype(float)
df["category"] = df["category"].str.upper()

df = df.drop_duplicates()

df.to_csv("data/processed/products_clean.csv", index=False)

print("Transformación completada")
