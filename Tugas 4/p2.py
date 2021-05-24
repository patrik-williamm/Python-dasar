	


	"""
	author patrik william
	follow ig @patrik_williamm
	git-hub patrik_williamm
	"""

karyawan = []
p = []
w = []
sma = []
s1 = []
d3 = []

isNext = True
while isNext:
	nama = input("masukan nama : ")

	jk = input("Gender p/w 	: ")


	karyawan.append(nama)

	if jk=="p":
		p.append(nama)
		pass
	elif jk=="w":
		w.append(nama)
		pass

    pdd = input("masukkan pedidikan(S1, D3, SMA)    : ")
    if pdd=="SMA":

    	pass
	ulangi = input("ulangi program y/n 	: ") 

	if ulangi=="y":
		isNext = True
		pass
	else :
		isNext = False
		pass
	pass

print("jumlah karyawan 	: ",len(karyawan))
print("pria : ",len(p))
print("wanita : ",len(w))