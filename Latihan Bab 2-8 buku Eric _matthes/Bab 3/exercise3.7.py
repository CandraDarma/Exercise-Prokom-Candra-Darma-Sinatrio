tamu = ["Kartini", "Albert Einstein", "Isaac Newton",
        "B.J. Habibie", "Marie Curie", "Nikola Tesla"]

print("Maaf, saya hanya bisa mengundang dua orang untuk makan malam.")
while len(tamu) > 2:
    dihapus = tamu.pop()
    print(f"Maaf {dihapus}, saya tidak bisa mengundang Anda makan malam.")

for orang in tamu:
    print(f"{orang}, Saya mengundang Anda untuk makan malam.")

del tamu[0]
del tamu[0]
print(tamu)