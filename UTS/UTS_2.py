from random import randint
print("1. Level 1 (Penjumlahan)")
print("2. Level 2 (Pengurangan)")
print("3. Level 3 (Perkalian)")
print("4. Exit")
level = int(input("Pilih Level: "))
lives = 3
score = 0
while True:
    if int(level) == 1:
        if lives > 0 and level == 1:
            x = randint(-100, 100)
            y = randint(-100, 100)
            z = x + y
            print({x},"+",{y})
            jawaban=int(input("jawabannya :"))
            if(jawaban==z):
                score+=2
            if (jawaban==z):
                print("Jawaban kamu benar!!",score,"life left:",lives)
            if(jawaban!=z):
                lives-=1
                score-=2
            if(jawaban!=z):
                print("Jawaban kamu salah!!",score,"life left:",lives)
            if(lives==0):
                print("Game Over!!, waahh kamu kurang beruntung coba lagi ??")
                break
    if int(level) == 2:
        if lives>0 and level==2 :
            x = randint(-100, 100)
            y = randint(-100, 100)
            z=x-y
            print({x},"-",{y})
            jawaban=int(input("jawabannya :"))
            if(jawaban==z):
                score+=2
            if (jawaban==z):
                print("Jawaban kamu benar!!",score,"life left:",lives)
            if(jawaban!=z):
                lives-=1
                score-=2
            if(jawaban!=z):
                print("Jawaban kamu salah!!",score,"life left:",lives)
            if(lives==0):
                print("Game Over!!, waahh kamu kurang beruntung coba lagi ??")
                break
    if int(level) == 3:
        if lives>0 and level==3 :
            x = randint(-100, 100)
            y = randint(-100, 100)
            z=x*y
            print({x},"*",{y})
            jawaban=int(input("jawabannya :"))
            if(jawaban==z):
                score+=2
            if (jawaban==z):
                print("Jawaban kamu benar!!",score,"life left:",lives)
            if(jawaban!=z):
                lives-=1
                score-=2
            if(jawaban!=z):
                print("Jawaban kamu salah!!",score,"life left:",lives)
            if(lives==0):
                print("Game Over!!, waahh kamu kurang beruntung coba lagi ??")
                break
    if int(level) == 4:
        exit()
    if int(level!=1) and (level!=2) and (level!=3) and (level!=4):
        print("tidak ada nihhh levelnyaa")
        break