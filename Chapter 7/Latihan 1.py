try:
    namafile= input('Masukkan Nama File: ')
    file=open(namafile,'r')
    print(file.read())
except FileNotFoundError:
    print('File tidak ditemukan')
