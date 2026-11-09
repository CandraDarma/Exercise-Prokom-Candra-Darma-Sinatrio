from pathlib import Path

path = Path(r"D:\Python 315 semester 1\Eric_Matthes\Bab 10\Exercise10.3\pi_digits.txt")
contents = path.read_text()


print("--- Program 1: cetak tiap baris ---")
for line in contents.splitlines():
    print(line)


print("\n--- Program 2: tanpa lstrip() ---")
pi_string = ""
for line in contents.splitlines():
    pi_string += line
print(pi_string)
print(len(pi_string))


print("\n--- Program 3: dengan lstrip() ---")
pi_string = ""
for line in contents.splitlines():
    pi_string += line.lstrip()
print(pi_string)
print(len(pi_string))