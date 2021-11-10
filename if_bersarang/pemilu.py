#Seleksi_Pemilu
#{I.S. : pengguna memasukkan umur dan status pernikahan}
#{F.S. : menampilkan boleh memilih atau tidak}

umur = int(input("Umur: "))
if (umur < 17):
    Menikah = input("Menikah [Y/T]  :  ").upper()
    if (Menikah == "Y"):
        print("Anda boleh ikut pemilu")
    else:
        print("Anda belum boleh ikut pemilu")
else:
    print("Anda boleh ikut pemilu")


