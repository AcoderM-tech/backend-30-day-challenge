#============================================================================================
# 1. Parol tekshiruvchi (shart, matn, ro'yxat)
# parol_tekshir(parol) -> list[str] xatolar ro'yxatini qaytarsin (bo'sh ro'yxat = parol yaxshi).
# Qoidalar: 8+ belgi, kamida bitta raqam, katta harf, kichik harf, bo'sh joy yo'q.

# parol_tekshir("abc")        # ["Kamida 8 belgi", "Raqam yo'q", "Katta harf yo'q"]
# parol_tekshir("Salom1234")  # []
#============================================================================================
import string
def parol_tekshir(matn):
    """Bu funksiya berilgan parolni quyidagi qoidalarga zid emasligini tekshiradi :
    Qoidalar: 8+ belgi, kamida bitta raqam, katta harf, kichik harf, bo'sh joy yo'q."""
    raqam = False
    belgi = False
    kattaharf = False
    kichkinaharf = False
    bosh_joy_bor = False
    xatolar=[]
    if not matn:
            xatolar.append("Parol mavjud emas !")
            return xatolar

    if len(matn)<8:
            xatolar.append("Parol uzunligi kamida 8 ta belgidan iborat bo'lishi kerak!!")
    for i in matn:
            if i.isspace():
                bosh_joy_bor=True
            if i.isdigit():
                raqam=True
            if i in string.punctuation:
                belgi = True
            if i.isupper():
                kattaharf=True
            if i.islower():
                kichkinaharf=True
    if not raqam:
            xatolar.append("Parol tarkibida raqam mavjud emas!!")
    if not belgi:
            xatolar.append("Parol tarkibida belgi mavjud emas!")
    if not kattaharf and not kichkinaharf:
        xatolar.append("Parol tarkibida harf mavjud emas!")
    else:
        if not kattaharf:
            xatolar.append("Parol tarkibida kattaharf mavjud emas!!")
        if not kichkinaharf:
            xatolar.append("Parol tarkibida kichkinaharf mavjud emas!!")
    if bosh_joy_bor:
            xatolar.append("Parol bo'sh joy mavjud bo'lmasligi kerak !!!")
    return xatolar
#tekshiruv
if "__main__" == __name__:
    print(parol_tekshir(""))
    print(parol_tekshir(" abshdsjd1 !"))
    print(parol_tekshir("a1!A"))
    print(parol_tekshir("parol2026"))
    print(parol_tekshir("KattaVaKichikHarf"))
    print(parol_tekshir("12345678!!!"))
    print(parol_tekshir("Uzbekistan_2026!"))

#==================================================================================
# 2. So'z hisoblagich (lug'at, tsikl, saralash)
# sozlar_soni(matn) -> dict har bir so'z necha marta uchrashini qaytarsin. Katta-kichik harf farqlanmasin, tinish belgilari (. , ! ?) hisobga olinmasin.
# Keyin top(natija, n): eng ko'p uchragan n ta so'zni (so'z, soni) ko'rinishida kamayish tartibida qaytarsin. Jadvalni f-string bilan chiqaring:
# So'z          Soni
# -----------------
# python           3
# men              2
#==================================================================================
def list_tozala(royxat):
    """Bu funksiya kirilgan dict elementlarini space va belgilardan tozalaydi,oxirida lower qilib toza dictni qaytaradi"""
    toza_royxat = []
    for element in royxat:
        toza_soz = ""
        for harf in element:
            if harf in string.punctuation:
                continue
            if harf.isdigit():
                continue
            if harf.isspace():
                continue
            toza_soz += harf
        toza_royxat.append(toza_soz.lower())

    return toza_royxat
def sozlar_soni(royxat):
    toza_royxat=list_tozala(royxat)
    tekshirilganlar=[]
    natija={}
    for asl_soz,soz in zip(royxat,toza_royxat):
        soni=0
        if soz in tekshirilganlar:
            continue
        else:
            tekshirilganlar.append(soz)
        for soz2 in toza_royxat:
            if soz==soz2:
                soni+=1
        natija[asl_soz]=soni

    return natija
test_list = [
    "  Salom123!",
    "Bu_matn_da2026",
    "Py@th*on  ",
    "salom...",
    "Bu_matn_da!!!",
    "  PY@TH*ON",
    "python123"
]
print(sozlar_soni(test_list))

#===================================================================================
#3. Tub sonlar va rekursiya (funksiya, for ... else, rekursiya)
# Uchta funksiya:
# tubmi(n) -> bool
# tublar(n) -> list[int]: n gacha hamma tub sonlar (ichida tubmi ishlatilsin)
# faktorial(n): rekursiya bilan. Manfiy son uchun ValueError.
#===================================================================================

#==================================================================================
#4. Xavfsiz kiritish va statistika (while, try/except, *args)
# son_ol(matn, minimum, maksimum) -> float: noto'g'ri yoki diapazondan tashqari bo'lsa qayta so'rasin.
# statistika(*sonlar) -> tuple: (soni, yig'indi, o'rtacha, eng_kichik, eng_katta) qaytarsin. min/max siz, tsikl bilan. Bo'sh chaqirilsa ValueError.
# main(): stop yozguncha son so'rasin (son_ol orqali emas, stop ham qabul qilinadi), oxirida natijani chiqarsin. Bo'sh bo'lsa dastur qulamasin.
# Maslahat: stop kiritilishi uchun son_ol ga yana bir parametr kerak bo'lishi mumkin, o'zingiz o'ylab toping.
#====================================================================================


#==================================================================================
# 5. Mini loyiha: talabalar baholari (hammasi birga)
# Terminal menyu:
# 1. Talaba qo'shish
# 2. Ball qo'shish
# 3. O'rtacha ballni ko'rish
# 4. Eng yaxshi 3 talaba
# 5. Hisobot
# 0. Chiqish
# Ma'lumot: {"Ali": [90, 85], "Vali": [70]}
# Talablar:
# Har bo'lim alohida funksiya.
# Menyu while True bilan, buyruqlar lug'at-funksiya usuli bilan boshqarilsin (amallar[belgi]() kabi).
# Takroriy ism, mavjud bo'lmagan talaba, 0-100 dan tashqari ball, bo'sh ro'yxat hollari dastur qulamasdan ishlansin.
# Hisobot f-string bilan tekis jadval bo'lsin:
# Ism        Ballar        O'rtacha   Baho
# ----------------------------------------
# Ali        90, 85           87.5      B
# Vali       70               70.0      C
# Baho funksiyasi: 90+ A, 80+ B, 70+ C, 60+ D, qolgani F.
#====================================================================================



