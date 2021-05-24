
#using module array

from array import array #import module array

a = array('i',[1,3,5])
#display array
print(a[0])


b = array('u',['p','a','t','r','i','k'])
#append for add array value
b.append('u')
print(b)

#append for add array value lebih dari 1
c = array('i',[1,2,3,4,5])
c.extend([6,7,8,9,10])
print(c)

d = array('i',[1,2,3,4,5])
d.insert(3,9)
print(d)


#megubah element lirik
e = array('d',[1.1,2.2,3.3])
e[1] = 1.2
print(e)

#menghapus elemen lirik
f = array('i',[1,2,3,4,5,6,7,8,9,0])
f.remove(0)
print(f)

p = f.pop()
print(p)

#megurutkan elemen larik
#function
g = array('i',[2,3,5,7,1])
def urutkan(x):
    for i in range(0, len(x)-2):
        for j in range(len(x)-1, i, -1):
            if x[j] < x[j-1]:
                #pertukarkan elemen lariknya
                x[j], x[j - 1] = x[j - 1], x[j]

#display output function
urutkan(g)
print(g)

#membalikan element larik
print(d)
d.reverse()
print(d)


#larik 2 dimensi

hours = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
print(hours)
print(hours[0][0])

#matriks
def matriks(y):
    for i in range(0, y.length):
        for j in range(0, i < j.length):
            y[j][i]
print(hours)
matriks(hours)
print(hours)




































  
