from string import punctuation
# 1. Soʻzlar hisoblagichi (sozlar_soni)
# Bu funksiyaga bitta uzun matn beriladi va siz u yerda har bir soʻz necha marta qatnashganini topishingiz kerak.
# • Katta-kichik harf farqlanmasin: Demak, matndagi "Olma" va "olma" soʻzlari bitta soʻz deb qaralishi kerak. Buning uchun hamma harflarni bir xil shaklga (masalan, kichik harfga) oʻtkazib olishingiz lozim.
# • Nuqta, vergul va belgilari oʻchirilsin: Masalan, "olma," (vergul bilan) va "olma" alohida soʻz boʻlib qolmasligi uchun, matndagi belgilarni (. , ! ?) toʻgʻrilab olish (tozalash) kerak.
# • Asosiy ish: Matnni alohida soʻzlarga ajratasiz (boʻlaklaysiz) va boya oʻrgangan .get(soʻz, 0) + 1 usulidan foydalanib, har bir soʻzni sanab, lugʻatga joylaysiz.
def sozlar_soni(matn):
    matn = matn.lower()
    yangimatn=""
    for harf in matn:
        if not harf in punctuation:
            yangimatn += harf
    royxat=yangimatn.split()
    natija={}
    for element in royxat:
            natija[element]=natija.get(element,0)+1
    return natija
test_matni = "Python, faqatgina Python! Bugun Python o'rganamiz... pyThon juda zo'r-da, to'g'rimi? BUGUN hamma python o'rganmoqda!"

lugat=sozlar_soni(test_matni)
# 2. Eng koʻp uchragan soʻz (top)
# Bu funksiya 1-mashqdagi tayyor natijani (lugʻatni) va n degan sonni qabul qiladi.
# • Vazifasi: Lugʻat ichidan eng koʻp marta takrorlangan n ta soʻzni topish. Masalan, n=3 boʻlsa, eng yuqori natija koʻrsatgan top-3 ta soʻzni ajratib olish kerak.
# • Jadval koʻrinishi: Topilgan natijalarni konsolga chiroyli, ustunma-ustun qilib chiqarish uchun f-string dagi textni tekislash (chapga/oʻngga surish, masalan {soz:<10}) imkoniyatlaridan foydalanishingiz talab etiladi.

def maxsoz(lugat):
    saralangan = sorted(lugat.items(), key=lambda x: x[1], reverse=True)
    print(f"{'Kalitlar':<10} | {'Qiymatlar':>10}")
    print("-" * 23)
    for qiymat in saralangan:
        print(f"{qiymat[0]:<10} | {qiymat[1]:>10}")
        print("-" * 23)

maxsoz(lugat)
# 3. Lugʻatlarni birlashtirish (birlashtir)
# Sizga ikkita tayyor lugʻat beriladi (masalan, ikkita doʻkondagi mevalar soni). Siz ularni bitta umumiy lugʻatga jamlashingiz kerak.
# • Mantiq: Agar biror meva (kalit) faqat bitta lugʻatda boʻlsa, u shundoq oʻtadi. Lekin ikkala lugʻatda ham bor boʻlsa (masalan, birida 1 ta, ikkinchisida 2 ta olma), ularning sonini (qiymatlarini) bir-biriga qoʻshib yozishingiz kerak (1 + 2 = 3).
def qoshaman(royxat1,royxat2):

    for kalit, qiymat in royxat2.items():
        if type(qiymat)==str:
           royxat1[kalit]=royxat1.get(kalit,'')+qiymat
        if type(qiymat)==int:
           royxat1[kalit]=royxat1.get(kalit,0)+qiymat
    return royxat1
lugat_a = {
    "olma": 5,
    "anor": 3,
    "salom": "Dunyo",
    "til": "Py"
}
lugat_b = {
    "olma": 2,
    "banan": 4,
    "salom": "lar",
    "til": "thon"
}
print(qoshaman(lugat_a, lugat_b))

# 4. Teskari lugʻat
# Lugʻatning ichidagi kalit va qiymatlarning oʻrnini almashtirish kerak. Yaʼni kalitlar qiymatga, qiymatlar esa kalitga aylanadi.
# Oʻylab koʻrish kerak boʻlgan joyi: Savolda aytilganidek, agar asl lugʻatda qiymatlar takrorlangan boʻlsa nima boʻladi? Masalan, {"ali": 5, "vali": 5} boʻlsa, teskari qilganda 5 degan kalitga qaysi ism yoziladi? Python-da bitta kalitga faqat bitta qiymat biriktirish mumkinligi sababli, oxirgi yozilgan ism oldingisini oʻchirib (yutib) yuboradi. Shuni inobatga olishingiz yoki qiymatlarni roʻyxat ichiga yigʻishingiz kerak boʻladi.

def teskarila(lugat):
    yangisi={}
    for kalit,qiymat in lugat.items():
        yangisi[qiymat]=yangisi.get(qiymat,[])+[kalit]

    return yangisi
# Test uchun ma'lumot (Asl lug'at)
# Bu yerda 5 soni (olma, anor) va 3 soni (banan, shaftoli) takrorlangan
test_lugat = {
    "olma": 5,
    "anor": 5,
    "banan": 3,
    "uzum": 4,
    "shaftoli": 3,
    "nok": 2
}


print(teskarila(test_lugat))

def taribla(royxat):
    tartiblangan={}
    for soz in royxat:
        bosh_harf=soz[0]
        tartiblangan[bosh_harf]=tartiblangan.get(bosh_harf,[])+[soz]
    return tartiblangan
test_sozlar = [
    "olma", "anor", "banan", "behi", "uzum",
    "olxo'ri", "nok", "shaftoli", "sabzi"
]

# Funksiyangizni tekshirish uchun:
print(taribla(test_sozlar))
