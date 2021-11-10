import math
# GajiLemburPegawai
# {I.S. : pengguna memasukan NIK, nama karyawan, golongan, jumlah jam kerja/bulan}
# {F.S. : menampilkan }

nik = int(input("Masukan NIK: "))
namaKaryawan = input("Masukan Nama Karyawan: ")
golongan = int(input("Masukan Golongan: "))
jumlahJamKerja = int(input("Masukan Jumlah Jam Kerja: "))
potonganJam = 10000
potonganhari = 50000
bonusLembur = 25000

# menentukan gaji pokok dan tunjangan
if golongan == 1:
    gaji = 1750000
    tunjangan = 0.125 * gaji
    besarTunjangan = 0.125
    tjg = "12.5%"
elif golongan == 2:
    gaji = 2300000
    tunjangan = 0.15 * gaji
    besarTunjangan = 0.15
    tjg = "15%"
else:
    print("Error, Golongan Tidak Ditemukan")

# Menentukan Lembur
maxJamKerja = 26 * 8   # total jam dalam 26 hari adalah 208 jam
diffJamKerja = jumlahJamKerja - maxJamKerja

totalUangLembur = 0
if diffJamKerja > 0:
  totalUangLembur= abs(diffJamKerja) * bonusLembur
else:
  totalUangLembur = 0

# Menentukan Potongan Gaji
if diffJamKerja < 0:
  totalPotongan = abs(diffJamKerja) * potonganJam
else:
  totalPotongan = 0

# Menghitung Gaji Bersih
totalTunjangan = math.floor(gaji * besarTunjangan)
totalPotongan = 0
gajihBersih = gaji + totalTunjangan + totalUangLembur - totalPotongan

print("Nomor Induk Karyawan     : ", nik)
print("Nama Karyawan            : ", namaKaryawan)
print("Golongan                 : ", golongan)
print("Jumlah Jam Kerja/Bulan   : ", jumlahJamKerja, "Jam")
print("Gaji Pokok               : ", gaji)
print(f"Tunjangan {tjg}         : ", totalTunjangan)
print("Lembur                       : ", diffJamKerja if diffJamKerja > 0 else 0, "Jam")
print("Uang Lembur              : ", totalUangLembur)
print("Potongan                 : ", totalPotongan)
print("Gaji Bersih              : ", gajihBersih)




