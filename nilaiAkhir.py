
nama = input("Masukkan Nama 	: ")
nilaiKeatifan = int(input("nilai Keatifan 	: "))
nilaiTugas = int(input("nilai Tugas 	: "))
nilaiUjian = int(input("nilai Ujian 	: "))

nilaMurniK = nilaiKeatifan * 20/100
nilaMurniT = nilaiTugas * 30/100
nilaMurniU = nilaiUjian * 50/100

nilaiAkhir = nilaMurniK + nilaMurniU + nilaMurniT
print("Nilai Akhir Mahasiswa = ",nilaiAkhir)