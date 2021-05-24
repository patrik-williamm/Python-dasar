
rows = int(input("masukkan jumlah baris : "))
cols = int(input("masukkan jumlah kolom  : "))

arr=[0]*rows
for i in range(rows):
	arr[i] = [arr]*cols
	for j in range(cols):
		arr[i][j]=(int(input("Masukkan element : ")))
		pass
	pass
print(arr)

a = 1
b = 1

arr2=[0]*a
for i in range(a):
	arr2[i] = [arr2]*cols
	for j in range(cols):
		arr2[i][j] = int(input("Tambah element : "))
		pass
	pass
arr.append(arr2)
print(arr)

arr.sort(arr2)
print(arr)

aa


