#[4, 7, 1, 9, 7, 3, 7] da 7 necha marta uchraydi va qaysi indekslarda?
def sana(royxat,son):
    indexlari=[]
    for i,x in zip(range(len(royxat)),royxat):
        if x==son:
            indexlari.append(i)
    return len(indexlari),indexlari
if __name__ == "__main__":
    a = [4, 7, 1, 9, 7, 3, 7]
    soni, indekslar = sana(a, 7)
    print(f"7 soni {soni} marta uchraydi. Indekslari: {indekslar}")

#Ro'yxatdan takrorlarni olib tashlang, tartib saqlansin (set siz).
def tozala(royxat):
    tozasi=[]
    for element in royxat:
        if element not in tozasi:
            tozasi.append(element)
    return tozasi
if __name__ == "__main__":
    test1 = [1, 2, 2, 3, 4, 4, 4, 5]
    test2 = ["olma", "anor", "olma", "banan", "anor", "olma"]
    test3 = [7, 7, 7, 7, 7, 7, 7]
    test4 = [10, 20, 30, 40, 50]
    test5 = []
    test6 = [1, "salom", 1, True, "salom", False, 0]

    print("Test 1:", tozala(test1))
    print("Test 2:", tozala(test2))
    print("Test 3:", tozala(test3))
    print("Test 4:", tozala(test4))
    print("Test 5:", tozala(test5))
    print("Test 6:", tozala(test6))
#1 dan 50 gacha 3 ga bo'linadigan sonlarning kvadratlari (comprehension bilan).
def kvadratla():
    return [x**2 for x in range(1,51) if x%3==0]

if __name__ == "__main__":
    print(kvadratla())
# #Shart: Sizga bitta sonlar roʻyxati va bitta k soni (surishlar soni) beriladi. Roʻyxat elementlarini oʻng tomonga qarab k marta surishingiz kerak. Roʻyxatning oxiridan chiqib ketgan elementlar uning boshiga kelib qoʻshilishi shart.
# • Cheklov: Yangi roʻyxat ochish mumkin emas! Amallar asl roʻyxatning oʻzida (joyida — in-place) bajarilishi kerak.
def suradi(royxat,k):
    i=0
    while i<k:
        harf=royxat.pop()
        royxat.insert(0,harf)
        i+=1
    return royxat
def suradi2(royxat,k):
    royxat[:]=royxat[-k:]+royxat[:-k]
    return royxat
#Shart: Roʻyxat ichida har xil sonlar, jumladan 0 (nol) sonlari ham bor. Siz hamma nollarni roʻyxatning eng oxiriga surishingiz kerak. Ammo noldan boshqa barcha sonlarning asl ketma-ketlik tartibi mutlaqo buzilmasligi shart.
#Cheklov: Yangi roʻyxat (masalan, tozasi = []) ochish taqiqlanadi! Hammasini oʻsha asl roʻyxat ichida hal qiling.
def nolsuradi(royxat):
    nol_index=0
    i=0
    while i<len(royxat):
        if royxat[i]!=0:
            royxat[i], royxat[nol_index] = royxat[nol_index], royxat[i]
            nol_index+=1
        i+=1
    return royxat
test = [0, 1, 0, 3, 12]
print(nolsuradi(test))

# 3-masala: "Maksimal foyda" (Best Time to Buy and Sell Stock)
#
# Shart: Sizga roʻyxat beriladi. Uning ichidagi sonlar aksiyaning kunlik narxlari (masalan, 0-kun, 1-kun, 2-kun...). Siz aksiyani qaysidir kuni sotib olib, undan keyingi kunlarning birida sotishingiz va eng katta foyda koʻrishingiz kerak. Eng maksimal foydani hisoblaydigan algoritm yozing. (Agar umuman foyda koʻrishning iloji boʻlmasa, ya'ni narx faqat tushib ketgan boʻlsa, 0 qaytarilsin).
# • Misol 1: [7, 1, 5, 3, 6, 4]
# 	• Natija: 5 boʻladi. (Chunki 2-kuni 1 soʻmga sotib olib, 5-kuni 6 soʻmga sotsangiz, 6 - 1 = 5 soʻm sof foyda boʻladi).
# • Misol 2: [7, 6, 4, 3, 1]
# 	• Natija: 0 boʻladi. (Chunki narxlar faqat tushgan, foyda qilib boʻlmaydi).
def foydachi(royxat):
    if not royxat:
        return 0
    maxfoyda=0
    minnarx=royxat[0]

    for i,x in enumerate(royxat):
        if minnarx>x:
            minnarx=x
        elif maxfoyda<x-minnarx:
            maxfoyda=x-minnarx
        else:
            continue
    return maxfoyda
print(foydachi([7, 1, 5, 3, 6, 4]))
print(foydachi([7, 6, 4, 3, 1]))


