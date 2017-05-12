#script by Muhamad Danil Rafiqi

def siapa():
	nama=raw_input("Masukkan Nama ")
	skill=" Cyber Security"
	danil=nama+" keahlian"+skill
	print danil
	return;
	
siapa()

def nyoba(s):
	luas=s*s;
	print luas;
	return;

s=input("Masukkan angka")
nyoba(s)

def cetak_biodata( nama, kota, umur=18):
	print "Nama : ", nama;
	print "Umur : ", umur;
	print "Kota : ", kota;
	return;

print "Tanpa memakai default argument : "
cetak_biodata("miki", 50, "bandung" )
