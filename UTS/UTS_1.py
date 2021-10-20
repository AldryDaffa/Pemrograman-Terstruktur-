tahun = int(input("Masukkan tahun: "))

if tahun % 400 == 0:
    print("{} merupakan tahun kabisat".format(tahun))
elif tahun % 100 == 0:
    print("{} bukan tahun kabisat".format(tahun))
elif tahun % 4 == 0:
    print("{} merupakan tahun kabisat".format(tahun))
else:
    print("{} bukan tahun kabisat".format(tahun))