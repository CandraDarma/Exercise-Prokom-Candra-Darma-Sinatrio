from pathlib import Path

name = input("Siapa nama kamu? ")

path = Path(r"D:\Python 315 semester 1\Eric_Matthes\Bab 10\Exercise10.4\guest.txt")
path.write_text(name)

print(f"Halo, {name}! Namamu sudah dicatat di {path}.")