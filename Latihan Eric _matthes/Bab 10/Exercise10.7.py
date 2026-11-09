print("Kalkulator penjumlahan. Ketik 'q' kapan saja untuk keluar.")

while True:
    first_number = input("\nAngka pertama: ")
    if first_number.lower() == "q":
        break

    second_number = input("Angka kedua: ")
    if second_number.lower() == "q":
        break

    try:
        total = int(first_number) + int(second_number)
    except ValueError:
        print("Maaf, kamu harus memasukkan angka bulat, bukan teks.")
    else:
        print(f"Hasilnya: {total}")