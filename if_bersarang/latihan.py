# UjianUlang
# {I.S. : pengguna memasukan nama, nilai matematika(nilaiMTK), nilai Bahasa Indonesia(nilaiBIND), nilai IPA(nilaiIPA), nilai Bahasa Inggris(nilaiBING), dan nilai standar kelulusan(nsk)}
# {F.S. : menampilkan mata pelajaran yang di remedial}

# Input
namaSiswa = input("Masukan Nama Siwa: ")
nilaiMTK = float(input("Masukan Nila Matematika: "))
nilaiBIndo = float(input("Masukan Nilai Bahasa Indonesia: "))
nilaiIPA = float(input("Masukan Nilai IPA: "))
nilaiBING = float(input("Masukan Nilai Bahasa Inggris: "))
nsk = float(input("Masukan Nilai Standar Kelulusan: "))

no = 1
# Proses
if(nilaiMTK >= nsk) and (nilaiBIndo >= nsk) and (nilaiIPA >= nsk) and (nilaiBING >= nsk):
    print("Selamat ", '"',namaSiswa,'"'," Kamu Lulus Semuanya")
elif (nilaiMTK < nsk) and (nilaiBIndo < nsk) and (nilaiIPA < nsk) and (nilaiBING < nsk):
    print("Maaf ", '"',namaSiswa,'"'," Seluruh Mata Pelajaran Harus Ikut Ujian Ulang")
else:
    print("Mata Pelajaran yang harus ", '"',namaSiswa,'"'," ikuti ujian ulang adalah: ")
    if nilaiMTK < nsk:
        print(no, "Matematika")
        no+=1
    if nilaiBIndo < nsk:
        print(no, "Bahasa Indonesia")
        no+=1
    if nilaiIPA < nsk:
        print(no, "IPA")
        no+=1
    if nilaiBING < nsk:
        print(no, "Bahasa Inggris")
        no+=1
