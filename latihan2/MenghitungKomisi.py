# Program Menghitung Komisi Salesman
# I.S. : Manginputkan nama salesman dan nilai penjualanya
# F.S. : Menampilkan nama salesman dan juga kondisi yang diperoleh 
## Latihan
# Input
nama      = str(input("Masukan Nama Salesman   : "))
penjualan = float(input("Masukan Hasil Penjualan : "))
# proses
komisi    = 0.05 * penjualan # 0.05 = 5%
# Output
print("Nama Salesman : ", nama)
print("Besar Komisi  : Rp.", komisi)