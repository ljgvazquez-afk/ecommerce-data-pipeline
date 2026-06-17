import pandas as pd

df = pd.read_csv("data/processed/products_clean.csv")

assert df["id"].is_unique, "IDs duplicados encontrados"
assert df["price"].isnull().sum() == 0, "Precios nulos encontrados"

print("Validaciones completadas correctamente")
