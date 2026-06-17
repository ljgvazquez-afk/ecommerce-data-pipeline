import requests
import pandas as pd
from pathlib import Path

URL = "https://fakestoreapi.com/products"

response = requests.get(URL, timeout=30)
response.raise_for_status()

df = pd.DataFrame(response.json())

Path("data/raw").mkdir(parents=True, exist_ok=True)
df.to_csv("data/raw/products.csv", index=False)

print(f"Productos extraídos: {len(df)}")
