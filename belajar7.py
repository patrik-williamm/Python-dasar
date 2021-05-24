

print("mengkonversi nilai jam, menit ke satuan detik")

jam = int(input("masukkan jam 	: "))
jam *= 3600
menit = int(input("masukkan menit 	: "));
menit *= 60
detik = int(input("masukkan detik 	: "));

print("\n")
detik += jam +  menit
print("luas persegi panjang adalah ",detik)


#konversi detik ke jam dan menit

print("mengkonversi nilai jam, menit ke satuan detik")

detik = int(input("masukkan detik 	: "))

if(detik >= 3600) :
	jam = detik/3600
	print("satuan jam 	= ",jam)
	pass
if (detik >= 60):
	menit = detik/60
	print("satuan menit 	= ",menit)
	pass
print("satuan detik 	= ",detik)
