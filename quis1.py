
jumlah_karyawan = int(input("jumlah karyawan	:"))

for i in range(0, jumlah_karyawan):
	nama = input("masukkan nama  : ")
	nip = int(input("masukkan nip : "))
	
	gajipokok = 900000
	tunjangan_keluarga = 0
	tunjangan_anak = 0
	
	status_nikah = input("apakah anda sudah menikah [m/b]	: ")
	
	if status_nikah == 'm':
	
		tunjangan_keluarga = 15/100 * gajipokok
		jumlahAnak = int(input("jumlah 	Anak 	: "))
		if jumlahAnak <= 3:
			tunjangan_anak = 5/100 * gajipokok
			pass
		pass
	
	elif status_nikah == 'b':
		
		tunjangan_anak = 0
		tunjangan_keluarga = 0
	
		pass
	
	gajiBersih = gajipokok + tunjangan_keluarga +tunjangan_anak
	tunjangan_keluarga
	
	
	print("\n\n -- DATA_NYA - KARYAWAN -- \n\n")
	print("Nama 			: ",nama)
	print("nik 			: ",nip)
	print("status_nikah 		: ",status_nikah)
	print("tunjangan_keluarga	: ",tunjangan_keluarga)
	print("tunjangan_anak 		: ",tunjangan_anak)
	print("gaji Bersih 		: ",gajiBersih)

	pass
print("\n\n DATA_NYA \n\n")
print("jumlah data yang input 	: ",jumlah_karyawan)
print("tunjangan_keluarga	: ",tunjangan_keluarga)
print("tunjangan_anak 		: ",tunjangan_anak)




