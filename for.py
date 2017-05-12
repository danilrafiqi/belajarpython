a=input("Nilai Awal : ")
b=input("Nilai Akhir : ")
jumlah=0
total=0
z="  "
print "Angka dimulai dari {}\nAngka diakhiri dari {}".format(a, b)
for i in range(a,(b+3)):
	print i
	jumlah=jumlah+1
	total=total+i
print "jumlah angka adalah {}\ntotal angka adalah {}".format(jumlah,total)
