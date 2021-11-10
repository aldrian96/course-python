# TiketKereta
#{I.S. : }
#{F.S. : }

# jktEkonomi = 100000
# jktBisnis = 400000
# jktEksekutif = 700000
#
# yogyaEkonomi = 200000
# yogyaBisnis = 500000
# yogyaEksekutif = 800000
#
# srbEkonomi = 300000
# srbBisnis = 600000
# srbEksekutif = 900000

print("Kode Kota: ")
print("1. Jakarta")
print("2. Yogyakarta")
print("3. Surabaya")
kota = int(input("Pilihan Kota [1/2/3]: "))

print("Kode Kelas: ")
print("1. Ekonomi")
print("2. Bisnis")
print("3. Eksekutif")
kelas = int(input("Pilihan Kelas [1/2/3]: "))

# diskon = 0
# Memilih Tiket Kota dan Kelasnya
if kota == "1":
    kota = "jakarta"
    if kelas == "1":
        kelas = "Ekonomi"
        hargaTiket = 100000
    elif kelas == "2":
        kelas = "Bisnis"
        hargaTiket = 400000
    elif kelas == "3":
        kelas = "Eksekutif"
        hargaTiket = 700000
    else:
        print("Kelas Dengan Kode Tersebut Tidak Ditemukan!")
elif kota == "2":
    kota = "Yogyakarta"
    if kelas == "1":
        kelas = "Ekonomi"
    elif kelas == "2":
        kelas = "Bisnis"
    elif kelas == "3":
        kelas = "Eksekutif"
    else:
        print("Kelas Dengan Kode Tersebut Tidak Ditemukan!")
elif kota == "3":
    kota = "Surabaya"
    if kelas == "1":
        kelas = "Ekonomi"
    elif kelas == "2":
        kelas = "Bisnis"
    elif kelas == "3":
        kelas = "Eksekutif"
    else:
        print("Kelas Tidak Ditemukan!")
else:
    print("Kota Dengan Kode Tersebut Tidak Ditemukan")

## Menentukan Banyak Tiket yang dibeli
# Jakarta
banyakTiket = int(input("Banyak Tiket: "))
if kota == "1" and kelas == "1":
    diskon = 0.1
    hargaTiket = 100000
    subTotal = 100000 * banyakTiket
    print("Harga Tiket: ", hargaTiket)
    print("Sub Total: ", subTotal)
elif kota == "1" and kelas == "2":
    diskon = 0.1
    hargaTiket = 400000
    subTotal = 400000 * banyakTiket
    print("Harga Tiket: ", hargaTiket)
    print("Sub Total: ", subTotal)
elif kota == "1" and kelas == "3":
    diskon = 0.1
    hargaTiket = 700000
    subTotal = 700000 * banyakTiket
    print("Harga Tiket: ", hargaTiket)
    print("Sub Total: ", subTotal)
else:
    print("Tolong Masukan Jumlah Tiket Yang Akan Dibeli Dengan Benar")

# Yogyakarta
if kota == "2" and kelas == "1":
    diskon = 0.1
    hargaTiket = 200000
    subTotal = 200000 * banyakTiket
    print("Harga Tiket: ", hargaTiket)
    print("Sub Total: ", subTotal)
elif kota == "2" and kelas == "2":
    diskon = 0.1
    hargaTiket = 500000
    subTotal = 500000 * banyakTiket
    print("Harga Tiket: ", hargaTiket)
    print("Subtotal: ", subTotal)
elif kota == "2" and kelas == "3":
    diskon = 0.1
    hargaTiket = 800000
    subTotal = 800000 * banyakTiket
    print("Harga Tiket: ", hargaTiket)
    print("Subtotal: ", subTotal)
else:
    print("Tolong Masukan Jumlah Tiket Yang Akan Dibeli Dengan Benar")

# Surabaya
if kota == "3" and kelas == "1":
    diskon = 0.1
    hargaTiket = 300000
    subTotal = 300000 * banyakTiket
    print("Harga Tiket: ", hargaTiket)
    print("Sub Total: ", subTotal)
elif kota == "3" and kelas == "2":
    diskon = 0.1
    hargaTiket = 600000
    subTotal = 600000 * banyakTiket
    print("Harga Tiket: ", hargaTiket)
    print("Subtotal: ", subTotal)
elif kota == "3" and kelas == "3":
    diskon = 0.1
    hargaTiket = 900000
    subTotal = 900000 * banyakTiket
    print("Harga Tiket: ", hargaTiket)
    print("Sub Total: ", subTotal)
else:
    print("Tolong Masukan Jumlah Tiket Yang Akan Dibeli Dengan Benar")






