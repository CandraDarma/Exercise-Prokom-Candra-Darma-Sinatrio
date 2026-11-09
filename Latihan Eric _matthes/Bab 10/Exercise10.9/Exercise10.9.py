from pathlib import Path

filenames = [r"D:\Python 315 semester 1\Eric_Matthes\Bab 10\Exercise10.9\cats.txt", r"D:\Python 315 semester 1\Eric_Matthes\Bab 10\Exercise10.9\dogs.txt"]

for filename in filenames:
    path = Path(filename)
    try:
        contents = path.read_text()
    except FileNotFoundError:
        pass            # gagal dengan diam-diam: tidak ada pesan apa pun
    else:
        print(f"\nIsi {filename}:")
        print(contents)