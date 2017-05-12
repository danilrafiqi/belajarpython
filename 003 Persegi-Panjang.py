#script by M. Danil Rafiqi

luas=""
keliling=""
pilih=""
p=""
l=""

print "Pilih Program yang akan digunakan\n1. Luas\n2. Keliling"
pilih=input("\nMasukkan Pilihan ")
if pilih==1:
	p=input("\nMasukkan Panjang ")
	l=input("Masukkan Lebar ")
	luas=p*l
	print "Luas dari persegi panjang yang panjangnya {} dan lebarnya {} adalah {}".format(p,l,luas)
else :
	p=input("\nMasukkan Panjang ")
	l=input("Masukkan Lebar ")
	keliling=(2*p)+(2*l)
	print "Keliling dari persegi panjang yang panjangnya {} dan lebarnya {} adalah {}".format(p,l,keliling)
