#Script by Muhamad Danil Rafiqi

print "Program Menghitung Pajak"
namabarang=raw_input("Masukkan Nama Barang ")
hargabarang=input("Masukkan Harga Barang ")
pajak=input("Masukkan Pajak(Dalam %) ")
pajak=hargabarang*pajak/100
bayar=hargabarang+pajak
print "Barang yang anda beli adalah {},dan anda harus bayar sebesar Rp.{}".format(namabarang,bayar)
