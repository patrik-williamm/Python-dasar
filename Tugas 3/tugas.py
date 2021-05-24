

def add(x, y):
	return x + y 
	pass

def kurang(x, y):
	return x - y
	pass

def kali(x, y):
	return x * y 
	pass

def bagi(x, y):
	return x / y 
	pass

def moduls(x, y):
	return x % y
	pass

bil1 = int(input("masukkan bil 1 	: "))
bil2 = int(input("masukkan bil 2 	: "))

option = input("masukkan pilihan [1..5]? : ")
if option == "1":
	print("Result 	: ",add(bil1, bil2))
	pass
elif option == "2":
	print("Result 	: ",kurang(bil1, bil2))
	pass
elif option == "3":
	print("Result 	: ",kali(bil1, bil2))
	pass
elif option == "4":
	print("Result 	: ",bagi(bil1, bil2))
	pass
elif option == "5":
	print("Result 	: ",moduls(bil1, bil2))

	pass
else :
	print("input tidak tersedia!!!")
	pass