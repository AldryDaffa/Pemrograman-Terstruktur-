def luassegitiga(a, t):
    luas = a * t / 2
    return luas


def hasil():
    print('luas segitiga degan alas ', alas,
          'dan tinggi ', tinggi,
          "adalah ", luassegitiga(alas, tinggi))


alas = 10
tinggi = 20
segitiga1 = luassegitiga(alas, tinggi)
hasil()

alas = 15
tinggi = 45
segitiga2 = luassegitiga(alas, tinggi)
hasil()
print("Total Luas Kedua segitiga =", segitiga1 + segitiga2)

