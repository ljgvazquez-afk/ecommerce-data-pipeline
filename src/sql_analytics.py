import pandas as pd

df = pd.read_csv("data/processed/products_clean.csv")

print("\nTOP 5 PRODUCTOS MÁS CAROS\n")

top_products = (
    df[["title", "price"]]
    .sort_values("price", ascending=False)
    .head(5)
)

print(top_products)

print("\nPRECIO PROMEDIO POR CATEGORÍA\n")

avg_price = (
    df.groupby("category")["price"]
    .mean()
    .sort_values(ascending=False)
)

print(avg_price)