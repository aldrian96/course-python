# MembacaNilaiUangDalamKelipatan25
# {I.S. : pengguna memasukan nominal uang(nilaiUang)}
# {F.S. : menampilkan hasil atau nilai penukaran rupiah}

# input
nilaiUang = int(input("Masukan Nominal Uang: "))

# proses
seribu = nilaiUang // 1000
sisaNilaiUang = nilaiUang % 1000
limaratus = sisaNilaiUang // 500
sisaNilaiUang = sisaNilaiUang % 500
seratus = sisaNilaiUang // 100
sisaNilaiUang = sisaNilaiUang % 100
limapuluh = sisaNilaiUang // 50
sisaNilaiUang =sisaNilaiUang % 50
dualima = sisaNilaiUang // 25
sisaNilaiUang = sisaNilaiUang % 25

# output
print("Nominal pecahan 1000: ", seribu)
print("Nominal pecahan 500: ", limaratus)
print("Nominal pecahan 100: ", seratus)
print("Nominal pecahan 50: ", limapuluh)
print("Nominal pecahan 25: ", dualima)
print("Sisa Nilai Uang: ", sisaNilaiUang)

