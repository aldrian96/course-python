# MengukurJarakSemutBerjalan
# {I.S. : pengguna memasukan jarak(jarak) semut berjalan menggunakan satuan cm}
# {F.S. : menampilkan hasil jarak tempuh semut berjalan}


jarak = int(input("Masukan Jarak Tempuh (cm): "))
km = jarak // 100000
sisaJarak = jarak % 100000
m = sisaJarak // 100
sisaJarak = sisaJarak % 100
cm = sisaJarak

print("Total km: ", km)
print("Total m: ", m)
print("Total cm: ", cm)