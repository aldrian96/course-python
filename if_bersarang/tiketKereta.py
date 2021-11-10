# TiketKereta
#{I.S. : }
#{F.S. : }

print("""Kode Kota : 
1. Jakarta
2. Yogyakarta
3. Surabaya""")
kodeKota = int(input("Pilihan Kota [1/2/3]: "))

print("""Kode Kelas :
1. Ekonomi
2. Bisnis
3. Eksekutif""")
kodeKelas = int(input("Pilihan Kelas [1/2/3]: "))

jumlahTiket = int(input("Masukkan Jumlah Tiket: "))
if (kodeKota == 1 ):
    if (kodeKelas == 1):
        hargaTiket = 100000
    elif (kodeKelas == 2):
        hargaTiket = 400000
    else:
        hargaTiket = 700000
elif (kodeKota == 2 ):
    if (kodeKelas == 1):
        kodePromo = str.upper((input("Masukkan Kode Voucher : ")))
        if (kodePromo == "PROMO"):
            diskon = 0.10
        else:
            diskon = 0
        hargaTiket = 200000
    elif (kodeKelas == 2):
        hargaTiket = 500000
    else:
        hargaTiket = 800000
else:
    if (kodeKelas == 1):
        hargaTiket = 300000
    elif (kodeKelas == 2):
        hargaTiket = 600000
    else:
        kodePromo = str.upper((input("Masukkan Kode Voucher : ")))
        if (kodePromo == "PROMO"):
            diskon = 0.10
        else:
            diskon = 0
        hargaTiket = 900000

subtotal = hargaTiket * jumlahTiket
hargaDiskon = diskon * subtotal
totalBayar = subtotal - hargaDiskon
print("Harga Tiket : Rp.",hargaTiket)
print("Sub Total : Rp.",subtotal)
print("Diskon : Rp.",hargaDiskon)
print("Total Bayar : Rp.",totalBayar)