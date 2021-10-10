import math
tarifawal = 200000
tariflanjutan = 10000
awalwaktu = 6.00
akhirwaktu = 23.50
durasiwaktu = math.ceil(akhirwaktu-awalwaktu)
lamawaktulanjutan = durasiwaktu - 12
tarifwaktulanjutan = lamawaktulanjutan * tariflanjutan
totalharga = tarifawal + tarifwaktulanjutan
print(totalharga)



