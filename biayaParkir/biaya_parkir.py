# MenghiutngBiayaParkir
# {I.S. : pengguna memasukan nomor polisi, jam masuk, menit masuk, jam keluar, menit keluar}
# {F.S. : menampilkan lamanya parkir dan biaya yang harus dibayar}

# Input
noPol = input("Masukan Nomor Polisi: ")
jamMasuk = int(input("Masukan Jam Masuk: "))
menitMasuk = int(input("Masukan Menit Masuk: "))
jamKeluar = int(input("Masukan Jam Keluar: "))
menitKeluar = int(input("Masukan Menit Keluar: "))

# mengecek jika jam keluar lebih kecil dari jam masuk
if jamKeluar < jamMasuk :
    jamKeluar = jamKeluar + 24 # 24 adalah format waktunya bisa 12 atau 24

# mengecek jika menit keluar lebih kecil dari menit masuk
if menitKeluar < menitMasuk:
    menitKeluar = menitKeluar + 60
    jamKeluar = jamKeluar - 1

# menghitung lamanya jam
jam = jamKeluar - jamMasuk

# menghitung lamanya menit
menit = menitKeluar - menitMasuk

# menghitung biaya parkir
biaya = 1500
if menit > 0:
    biaya = biaya + jam * 500

# Output
print("Nomor Polisi : ", noPol)
print("Jam Masuk    : ", jamMasuk)
print("Menit Masuk  : ", menitMasuk)
print("Jam keluar   : ", jamKeluar)
print("Menit Keluar : ", menitKeluar)
print("Lama Parkir  : ", jam, "Jam", menit, "Menit")
print("Biaya Parkir : ", biaya)