#script By Muhamad Danil Rafiqi

print "Versi 1"
nama=raw_input("Masukkan Nama : ")
namabaru=nama[::-1]

print nama
print namabaru

print "\nVersi 2"
nama=raw_input("Masukkan Nama : ")
namabaru=list(nama)
namabaru.reverse()

print nama
print namabaru
print "".join(namabaru)

print "\nVersi 3"
nama=raw_input("Masukkan Nama : ")
namabaru="".join(reversed(nama))

print nama
print namabaru
