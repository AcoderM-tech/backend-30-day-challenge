#=======================================================================================
try:
    a = int(input("Sonni kiriting: "))
    if a < 2:
        raise ValueError("Son 2 yoki undan katta bo'lishi kerak")
except ValueError as ve:
    print(f"Xatolik: {ve}")
else:
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            print(f"{a} soni tub emas")
            break
    else:
        print(f"{a} soni tub")
#========================================================================================
sonlar=[]

while True:
    a=input("Sonni kiriting (to'xtatish uchun stop):").strip().lower()
    if a=="stop":
        break
    try:
        a = float(a)
        sonlar.append(a)
    except ValueError as ve:
        print(f"Xatolik:{ve}")
if sonlar:
    yigindi = sum(sonlar)
    ortacha = yigindi / len(sonlar)
    print(f"\nSonlar soni: {len(sonlar)}")
    print(f"Yig'indi: {yigindi:g}")
    print(f"O'rtacha: {ortacha:.2f}")
else:
    print("Hech narsa kiritilmadi")

#===============================================================================================


# ================================================================
#1 dan 100 gacha juft sonlar yig'indisini topishni sodda versiyasi
s=0
for i in range(2,101,2):
    s+=i
print(f"100 gacha juft sonlar yig'indisi:{s}")
#1 dan 100 gacha juft sonlar yig'indisini 2-ideal versiyasi
print(f"100 gacha juft sonlar yig'indisi:{sum(range(2,101,2))}")
#================================================================
#Ro'yxatdagi eng katta sonni max() siz toping
import random as r
sonlar=[]
for i in range(15):
    sonlar.append(r.randint(1,100))
print("Ro'yxat:", sonlar)
b=sonlar[0]
for a in sonlar:
    if a>b:
        b=a
print("Eng katta son:", b)
# ====================================================================
# uchta sondan kattasini qaytaruvcghi funksiya
def max_top(a, b, c):
    sonlar = [a, b, c]
    for i in sonlar:
        if i > a:
            a = i
    return a

print(max_top(45, -455, 4))
#======================================================================
#Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir matnning birinchi harfini katta harfga o'zgatiruvchi funksiya yozing.
def katta_qil(matnlar):
    matnlarv1=[]
    for a in matnlar:
        matnlarv1.append(a.title())
    return matnlarv1
matn=['olma','olma','olma']
print(katta_qil(matn))
print(matn)
