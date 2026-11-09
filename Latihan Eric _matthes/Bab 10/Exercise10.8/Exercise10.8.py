from pathlib import Path

filenames = [r"D:\Python 315 semester 1\Eric_Matthes\Bab 10\Exercise10.8\dogs.txt", r"D:\Python 315 semester 1\Eric_Matthes\Bab 10\Exercise10.8\cats.txt"]

for filename in filenames:
    path = Path(filename)
    try:
        contents = path.read_text()
    except FileNotFoundError:
        print(f"Maaf, file {filename} tidak ditemukan.")
    else:
        print(f"\nIsi {filename}:")
        print(contents)