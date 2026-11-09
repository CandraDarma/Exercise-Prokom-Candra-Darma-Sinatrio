from pathlib import Path

path = Path(r"D:\Python 315 semester 1\Eric_Matthes\Bab 10\Exercise10\learning_python.txt")


print("--- Cara 1: read_text() ---")
contents = path.read_text()
print(contents)


print("--- Cara 2: list of lines ---")
lines = contents.splitlines()
for line in lines:
    print(line)