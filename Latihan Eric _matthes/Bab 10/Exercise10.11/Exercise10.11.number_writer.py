import json
from pathlib import Path

number = input("Berapa angka favoritmu? ")

path = Path("favorite_number.json")
path.write_text(json.dumps(number))

print("Angka favoritmu sudah disimpan.")