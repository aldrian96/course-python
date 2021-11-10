# program untuk menukar nilai
# I.S : dibikan dua angka terhadap variabel angka 1=5 dan angka 2=2
# F.S : Menampilkasn hasil pertukaran 

angka1 = int(input("Masukan angka 1: "))   
angka2 = int(input("masukan angka 2: "))

# menampilkan nilai sebelum ditukar
print("===== Nilai sebelum ditukar =====")
print("Nilai angka 1: ",angka1)
print("Nilai angka 2: ",angka2)

# Proses pertukaran
angka3 = angka1
angka1 = angka2
angka1 = angka3

# menampilkan angka setelah ditukar
print("==== Nilai setelah ditukar =====")
print(angka1)
print(angka2)