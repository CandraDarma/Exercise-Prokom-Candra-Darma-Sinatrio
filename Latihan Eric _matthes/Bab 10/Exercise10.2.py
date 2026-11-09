from pathlib import Path

path = Path(r"D:\Python 315 semester 1\Eric_Matthes\Bab 10\Exercise10\learning_python.txt")
contents = path.read_text()

for line in contents.splitlines():
    print(line.replace("Python", "C"))