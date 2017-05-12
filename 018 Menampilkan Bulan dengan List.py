#script by Muhamad Danil Rafiqi
pilih = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
a=input("Masukkan Pilihan 1-12 : ")
if (a>=1 and a<=12):
	print "Bulan yang anda pilih adalah ",pilih[a-1]
else :
	print"Masukkan angka 1-12"
print pilih
del pilih[1]
print pilih
del pilih[2:5]
print pilih
del pilih

