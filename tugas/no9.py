# MengkonversiPanjangBendaDariMeterKeInc
# {I.S.  : memkonversi panjang awal sebuah  benda dalam satuan meter ke inci }
# {F.S. : menampilkan hasil konversi dari meter ke inci}

totalMeter = float(input("Masukan Total Meter: "))

mm = totalMeter * 1000
cm = totalMeter * 100
inchi = mm / 25.4
kaki = cm / 30.48
yard = totalMeter / 0.9144

print("{:.2f}".format(inchi))
print("{:.2f}".format(kaki))
print("{:.2f}".format(yard))