#Script By Muhamad Danil Rafiqi

print "Program Penggunaan If bersarang"
print "Script by M. Danil Rafiqi\n"
print "Kamu mau makan apa minum ???\n1.Makan\n2.Minum"

jawaban=input("Masukkan pilihan")
if (jawaban==1):
	print "Kamu mau makan apa??\n1.Sate\n2.Bakso"
	jawab=input("Masukkan pilihan")
	if jawab==1 :
		print "Kamu mau makan sate"
	else :
		print "Kamu mau makan bakso"
else:
	print "Kamu mau minum apa???\n1.Es Teh\n2.Jus"
	jwb=input("Masukkan pilihan")
	if jwb==1:
		print "Kamu mau minum es teh"
	else :
		print "Kamu mau minum jus"
