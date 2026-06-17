import requests
import pandas as pd
from pathlib import Path

URL = "https://fakestoreapi.com/users"

response = requests.get(URL, timeout=30)
response.raise_for_status()

df = pd.DataFrame(response.json())

Path("data/raw").mkdir(parents=True, exist_ok=True)

df.to_csv("data/raw/users.csv", index=False)

print(f"Usuarios extraídos: {len(df)}")