data = open('D:\ biodata.txt', 'r')

baca = data.readlines()

hasil = []
for i in range(len(baca)):
    baca2 = {}
    fix= baca[i] .replace('\n ', '')
    fix2= fix.split("|")
    baca2['nim']=fix2[0]
    baca2['nama'] = fix2[1]
    baca2['alamat'] = fix2[2]
    hasil+=[baca2]

print (hasil)
data.close()
