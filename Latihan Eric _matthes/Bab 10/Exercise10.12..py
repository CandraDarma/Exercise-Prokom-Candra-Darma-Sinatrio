import json
from pathlib import Path

path = Path("favorite_number.json")

if path.exists():
    number = json.loads(path.read_text())
    print(f"I know your favorite number! It's {number}.")
    pilihan = input("Apakah ingin reset?(y/n): ")
    if pilihan.lower() == 'y' :
        path.unlink()
        print("Angka Favoritmu telah dihapus")


else:
    number = input("Berapa angka favoritmu? ")
    path.write_text(json.dumps(number))
    print("Oke, angka favoritmu sudah kuingat!")