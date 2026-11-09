import json
from pathlib import Path

path = Path("user_info.json")

if path.exists():
    user = json.loads(path.read_text())
    print("Ini yang saya ingat tentang kamu:")

for key, value in user.items():
    print(f"- {key}: {value}")

    pilihan = input("Apakah ingin reset?(y/n): ")
    if pilihan.lower() == 'y' :
                    path.unlink()
                    print("Datamu telah dihapus")

else:
    user = {
        "name": input("Siapa namamu? "),
        "city": input("Kamu tinggal di kota mana? "),
        "hobby": input("Apa hobimu? "),
    }

    path.write_text(json.dumps(user))
    
    print("\nInformasi kamu sudah disimpan. Ini ringkasannya:")


for key, value in user.items():
    print(f"- {key}: {value}")