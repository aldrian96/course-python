# MenghitungJarakHari
# {I.S.	: Pengguna memasukan hari(hari1), bulan(bulan1), tahun(tahun1) pertama dan hari(hari2), bulan(bulan2), tahun(tahun2) kedua}
# {F.S.	: Menampilkan selisih hari dari kedua tanggal tersebut}

# Input
hari1 = int(input("Hari pertama: "))
bulan1 = int(input("Bulan Pertama: "))
tahun1 = int(input("Tahun Pertama: "))

# Proses
hari2 = int(input("Hari kedua: "))
bulan2 = int(input("Bulan Kedua: "))
tahun2 = int(input("Tahun Kedua: "))

hari3 = hari2 - hari1
bulan3 = (bulan2 - bulan1) * 30 
tahun3 = (tahun2 - tahun1) * 365

selisih_hari = hari3 + bulan3 + tahun3

# Output
print("Selisih Hari: ", selisih_hari)


