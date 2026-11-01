Nama = ["Candra", "Sultan", "Rafel"]
Nama.append("Candi")        # tambah di akhir
Nama.insert(0, "Neejad")    # sisip di posisi tertentu
print(Nama)

Nama.remove("Candi")        # hapus berdasarkan nilai
last = Nama.pop()           # hapus dan ambil elemen terakhir
print(last)
del Nama[0]                 # hapus berdasarkan index
print(Nama)

Nama.sort()                 # urutkan permanen
print(Nama)
print(sorted(Nama, reverse=True))   # urutkan sementara
Nama.reverse()              # balik urutan
print(Nama)
print(len(Nama))            # jumlah elemen
