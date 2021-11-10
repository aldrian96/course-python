nik = int(input("Masukan NIK: "))
namaKaryawan = input("Masukan Nama Karyawan: ")
golongan = int(input("Masukan Golongan: "))
jumlahJamKerja = int(input("Masukan Jumlah Jam Kerja: "))


def hitungGajiBersih(gaji, tunjangan, jamKerja):
    potongan = 0
    lembur = 0
    jumlahJamLembur = jamKerja - (26 * 8)
    jumlahJamPotongan = (26 * 8) - jamKerja
    hariLembur = 0
    hariPotongan = 0

    if jamKerja > (26 * 8):
        lembur = (jamKerja - (26 * 8)) * 25000
        while jumlahJamLembur >= 8:
            jumlahJamLembur -= 8
            hariLembur += 1
    if jamKerja < (26 * 8):
        while jumlahJamPotongan >= 8:
            jumlahJamPotongan -= 8
            hariPotongan += 1
        potongan = (jumlahJamPotongan * 10000) + (hariPotongan * 50000)

    gajiBersih = gaji + tunjangan + lembur - potongan

    print("Nomor Induk Karyawan     : ", nik)
    print("Nama Karyawan            : ", namaKaryawan)
    print("Golongan                 : ", golongan)
    print("Jumlah Jam Kerja/Bulan   : ", jamKerja, " Jam")
    print("Gaji Pokok               : ", gaji)
    print("Tunjangan                : ", tunjangan)
    print("Lembur                   : ", jumlahJamLembur, " Jam")
    print("                         : ", hariLembur, " Hari", jumlahJamLembur, " Jam")
    print("                         : ", lembur)
    print("Potongan                 : ", jamKerja, " Jam")
    print("                         : ", hariPotongan, " Hari", jumlahJamPotongan, " Jam")
    print("                         : ", potongan)
    print("Gaji Bersih              : ", gajiBersih)


if golongan == 1:
    gaji = 1750000
    tunjangan = 0.125 * gaji
    besarTunjangan = "12.5%"
    hitungGajiBersih(gaji, tunjangan, jumlahJamKerja)
elif golongan == 2:
    gaji = 2300000
    tunjangan = 0.15 * gaji
    besarTunjangan = "15%"
    hitungGajiBersih(gaji, tunjangan, jumlahJamKerja)
else:
    print("Error, Golongan Tidak Valid")