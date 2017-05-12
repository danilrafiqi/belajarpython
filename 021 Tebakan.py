#script by Muhamad Danil Rafiqi
nomer=22
tebak=""
while (tebak!=nomer):
	tebak=input("Masukkan tebakkan Kamu : ")
	if tebak>nomer:
		print "tebakan kamu terlalu besar"
	elif tebak<nomer:
		print "tebakan kamu terlalu kecil"
print "yee jawaban kamu bener"	
