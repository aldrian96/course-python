# MenukarNilaiBilangan
# {I.S.	: Pengguna memasukan nilai kesatu(x), kedua(y), ketiga(z)}
# {F.S.	: Menampilkan hasil pertukaran nilai kesatu(x), kedua(y), ketiga(z)}

# Input
x = int(input("Masukan Nilai x: "))
y = int(input("Masukan Nilai y: "))
z = int(input("Masukan Nilai z: "))

# Output
print("x y z")
print(x, y, z)

# Proses
n = x
x = y
y = z
z = n

# Output
print("y z x")
print(x, y, z)