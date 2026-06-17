import pandas as pd

products = pd.read_csv("data/processed/products_clean.csv")

print("\n===== RESUMEN DE NEGOCIO =====\n")

print(f"Total productos: {len(products)}")

print(f"Precio promedio: ${products['price'].mean():.2f}")

print(f"Precio máximo: ${products['price'].max():.2f}")

print(f"Precio mínimo: ${products['price'].min():.2f}")

print("\nProductos por categoría:\n")

print(products["category"].value_counts())