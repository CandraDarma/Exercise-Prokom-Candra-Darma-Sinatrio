tamu = ["Albert Einstein", "Soekarno", "Yati"]
for orang in tamu:
    print(f"Yth. {orang}, silahkan datang ke acara makan malam.")

print(f"\n{tamu[1]} tidak bisa hadir.")
tamu[1] = "B.J. Habibie"

for orang in tamu:
    print(f"Yth. {orang}, silahkan datang ke acara makan malam.")