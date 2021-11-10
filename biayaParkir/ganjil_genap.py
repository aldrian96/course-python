# Algoritma BilanganGenap
# {I.S. : pengguna memasukan sebuah bilangan}
# {F.S. : menampilkan keterangan bilangan genap / ganjil}

Bilangan = int(input("Masukan Sebuah Bilangan: "))

if (Bilangan % 2 == 0) :
    Keterangan = "Bilangan Genap"
else :
    Keterangan = "Bilangan Ganjil"

print(Keterangan)
