
print("\n\n-- MASUKKAN WAKTU MULAI KULIAH --\n\n");

ml_jam = int(input("Masukkan jam mulai 		: "));
ml_menit = int(input("Masukkan menit mulai 		: "));
ml_detik = int(input("Masukkan detik mulai 		: "));


print("\n\n-- MASUKKAN WAKTU SELESAI KULIAH --\n\n");

sl_jam = int(input("Masukkan jam selesai 		: "));
sl_menit = int(input("Masukkan menit selesai 		: "));
sl_detik = int(input("Masukkan detik selesai 		: "));


print("\n\n-- DURASI WAKTU PERKULIAHAN --\n\n");

jam = sl_jam -ml_jam
menit = 0

if ml_menit < sl_menit:
	menit = ml_menit - sl_menit 
	pass
elif ml_menit >= sl_menit:
	menit = sl_menit - ml_menit
	pass
print("DURASI jam 	: ",jam," jam")
print("DURASI menit 	: ",menit," menit")
# print("DURASI detik 	: ",detik," detik")
