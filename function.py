
panjang = lebar = luas = 0

def inputData(x, y) :
	global panjang, lebar
	panjang = int(input("masukkan panjang %s	; " %x))
	lebar = int(input("masukkan lebar 	%s	: " %y))
	pass

def hitLuas():
	ls = panjang * lebar
	return ls
	pass
	
def cetak():
	print("luas adalah = %4d m2" %luas)
	pass

#input data dan hitung luas bidang 1 
inputData('(a)', '(b)')
luas = hitLuas()

#input data dan hitung luas bidang 2
inputData('(c)', '(d)')
luas += hitLuas()

#tampilkan
cetak()