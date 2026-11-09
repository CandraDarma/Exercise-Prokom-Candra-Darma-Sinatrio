from pathlib import Path

names = []

while True:
    name = input("Masukkan nama tamu (ketik 'q' untuk selesai): ")
    if name.lower() == "q":
        break
    names.append(name)

# "\n".join(names) menyambung semua nama dengan baris baru di antaranya
contents = "\n".join(names)
Path(r"D:\Python 315 semester 1\Eric_Matthes\Bab 10\Exercise10.5\guest.txt").write_text(contents)

print(f"{len(names)} nama disimpan di guest_book.txt")