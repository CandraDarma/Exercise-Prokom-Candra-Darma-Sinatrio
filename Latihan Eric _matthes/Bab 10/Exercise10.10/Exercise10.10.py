from pathlib import Path


def count_word(path, word):
    """Hitung kira-kira berapa kali sebuah kata muncul di dalam file."""
    try:
        contents = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"Maaf, file {path} tidak ditemukan.")
        return

    count = contents.lower().count(word)
    print(f"Kata '{word}' muncul sekitar {count} kali di {path}.")


# Ganti nama file di bawah ini dengan teks Project Gutenberg milikmu
filenames = [r"D:\Python 315 semester 1\Eric_Matthes\Bab 10\Exercise10.10\gutenberg.txt"]

for filename in filenames:
    path = Path(filename)
    count_word(path, "that")         # juga menghitung 'then', 'there', 'they'
    count_word(path, "the ")        # dengan spasi: "then" tidak ikut terhitung