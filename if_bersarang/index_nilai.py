# Menentukan Index Nilai
# {I.S. : Pengguna Memasukan Sebuah Nilai}
# {F.S. : Menampilkan Index Nilai/Nilai Mutu}

# Input
nilai = float(input("Masukan Nilai: "))

# Proses
if (nilai >= 80) and (nilai <= 100):
    indeks = "A"
elif (nilai >= 70) and (nilai < 80):
    indeks = "B"
elif (nilai >= 60) and (nilai < 70):
    indeks = "C"
elif (nilai >= 50) and (nilai < 60):
    indeks = "D"
else:
    indeks = "E"

# Output
print("Nilai Indeks: ", indeks)