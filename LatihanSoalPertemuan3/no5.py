# MenghitungJarakAntaraDuaTanggal
# {I.S.	: Pengguna memasukan hari pertama(hari1), bulan pertama(bulan1), tahun pertama(tahun1) dan hari kedua(hari2), bulan kedua(bulan2), tahun kedua(tahun2)}
# {F.S.	: Menampilkan selisih hari dari kedua tanggal tersebut}

# Input
hari1  = int(input("Hari pertama: "))
bulan1 = int(input("Bulan Pertama: "))
tahun1 = int(input("Tahun Pertama: "))
hari2  = int(input("Hari kedua: "))
bulan2 = int(input("Bulan Kedua: "))
tahun2 = int(input("Tahun Kedua: "))
# Proses
hari = (hari2 - hari1) + (bulan2 - bulan1) * 30 + (tahun2 - tahun1) * 365

tahun = hari // 365
sisa  = hari % 365
bulan = sisa // 30
hari  = sisa % 30

# Output
print("Jarak Antara Kedua Tanggal: ", tahun, "Tahun", bulan,"Bulan", hari, "Hari")