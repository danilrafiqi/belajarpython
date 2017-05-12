#script by Muhamad Danil Rafiqi
import datetime


print "=========================="
print "Hitung IPK"
print "==========================\n"

def hitung():
	nama=raw_input("Masukkan Nama ")
	algo=input("Masukkan Nilai Algoritma ")
	itcs=input("Masukkan Nilai Introduction to Cyber Security ")
	pti=input("Masukkan Nilai PTI ")

	IPK=(algo+itcs+pti)/3
	print "IPK yang di peroleh {} adalah {}\n".format(nama,IPK)
	return

for a in range(1,4):
	hitung()
