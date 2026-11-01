tamu = ["Albert Einstein", "B.J. Habibie", "Marie Curie"]

# Undangan awal
for orang in tamu:
    print(f"Yth. {orang}, silakan datang ke acara makan malam.")

print("\nSaya ingin mengundang beberapa tamu tambahan!\n")

# Tambah tamu baru
tamu.insert(0, "Kartini")
tamu.insert(2, "Isaac Newton")
tamu.append("Nikola Tesla")

# Undangan untuk daftar tamu yang sudah diperbarui
for orang in tamu:
    print(f"Yth. {orang}, silakan datang ke acara makan malam.")