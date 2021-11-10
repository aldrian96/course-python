# MenghitungLamaPengerjaanProyek
# {I.S.	: Mengkonversi akumulasi Hari(hari), Bulan(bulan), Tahun(tahun) sebuah proyek dengan pengguna memasukan jumlah hari(x)}
# {F.S.	: Menampilkan hasil conversi lama proyek tersebut dikerjakan}

# Input
x = int(input("Masulan jumlah hari: "))

# Algoritma
tahun = x // 365
sisa = x % 365
bulan = sisa // 30
hari = sisa % 30

# Output
print(tahun,"Tahun ", bulan,"Bulan ", hari,"Hari")
