# MenukarNilaiTigaVariable
# {I.S.	: Pengguna memasukan nilai kesatu(x), kedua(y), ketiga(z), (n) adalah wadah tambahan}
# {F.S.	: Menampilkan hasil pertukaran nilai kesatu(x), kedua(y), ketiga(z)}

# Input
x = int(input("Masukan Nilai x: "))
y = int(input("Masukan Nilai y: "))
z = int(input("Masukan Nilai z: "))

# Proses
n = x
x = y
y = z
z = n

# Output
print("Nilai x = ", x)
print("Nilai y = ", y)
print("Nilai z = ", z)