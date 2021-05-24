


print("\n\n\tPROGRAM HITUNG GAJI KARYAWAN PT. STMIK DP")
print("--------------------------------------------\n")

isStop = True
while isStop:

	nip = int(input("\tMasukkan Nip 	\t\t\t\t: "))
	nama = input("\tMasukkan Nama 	\t\t\t\t: ")

	gol = input("\tMasukkan Gol(I, II, III, IV)	\t\t: ")

	gaji_pokok=0

	if gol=="I":
		gaji_pokok = 2_000_000
		pass
	elif gol=="II":
		gaji_pokok = 2_500_000
		pass
	elif gol=="III":
		gaji_pokok = 3_000_000
		pass
	elif gol=="IV":
		gaji_pokok = 3_500_000
		pass
	else:
		print("\tGol no find!!!")
		pass


	kd_jabatan = input("\tMasukkan Kode Jabatan(D, M, K, B, S, N) 	: ")
	nm_jabatan = "";
	tj_jabatan = 0
	if kd_jabatan=="D":
		nm_jabatan = "DIREKTUR"
		tj_jabatan = 5_000_000
		pass
	elif kd_jabatan=="M":
		nm_jabatan = "MANAGER"
		tj_jabatan = 4_000_000
		pass
	elif kd_jabatan=="K":
		nm_jabatan = "KEPALA BAGIAN"
		tj_jabatan = 3_000_000
		pass
	elif kd_jabatan=="B":
		nm_jabatan = "BENDAHARA"
		tj_jabatan = 3_000_000
		pass
	elif kd_jabatan=="S":
		nm_jabatan = "SEKERTARIS"
		tj_jabatan = 3_000_000
		pass
	elif kd_jabatan=="N":
		nm_jabatan = "NON jabatan"
		tj_jabatan = 0
		pass
	else:
		print("\tfailed data")
		pass

	st_kawin = input("\tMasukkan Status Kawin(K/T) 	\t\t: ")
	tj_klg = 0

	if st_kawin=="K" :
		tj_klg = 10/100 * gaji_pokok
		pass
	elif st_kawin!="K" or st_kawin=="T":
		tj_klg = 0
		pass
	else:
		print("\tinput anda salah")

	hit_tGaji = gaji_pokok + tj_klg + tj_jabatan
	pph = 10/100 * hit_tGaji
	gaji_bersih = hit_tGaji - pph

	print("\n----------SLIP GAJI KARYAWAN-----------------\n")
	print("\tNip					: ", nip)
	print("\tNama 					: ", nama)
	print("\tGol[I, II, III, IV] 		\t: ", gol)
	print("\tKode jabatan(D,M,K,B,S,N) 	\t: ", kd_jabatan)
	print("\tStatus Kawin(K/T) 			: ", st_kawin)
	print("\tGaji Pokok 				: ", gaji_pokok)
	print("\tJabatan 				: ", nm_jabatan)
	print("\tTunjangan Jabatan 			: ", int(tj_jabatan))
	print("\tTunjangan Keluarga			: ", int(tj_klg))
	print("\tTotal Gaji 				: ", int(hit_tGaji))
	print("\tPotongan PPH 				: ", int(pph))
	print("\tGaji Bersih 				: ", int(gaji_bersih))

	ulangi = input("\n\n\tulangi program y/t 	: ")
	if ulangi=="y":
		isStop=True
		pass
	elif ulangi=="t":
		isStop=False
		pass
	else:
		print("\tMasukkan anda salah!!!")
	pass
