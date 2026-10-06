#FIZZ BUZZ o'yining eng sodda versiyasi
a=int(input("Sonni kiriting 1 dan  9 gacha :"))
b=int(input("Boshqa sonni kiriting 1 dan 9 gacha :"))
if a==b:
     print("Aka sizga turli xil son kirit degandimku")
     exit()
if not (1 <= a <= 9 and 1 <= b <= 9):
    print("Sonlar 1 dan 9 gacha bo'lishi kerak")
    exit()
for i in range(1,101):
    if i%a==0 and i%b==0:
        print("FIZZBUZZ")
    elif i%a==0:
        print("FIZZ")
    elif i%b==0:
        print("BUZZ")
    else:
        print(i)
#2-versiyasi
def chiqar(a,b):
    for i in range(1, 101):
        if i % a == 0 and i % b == 0:
            print("FIZZBUZZ")
        elif i % a == 0:
            print("FIZZ")
        elif i % b == 0:
            print("BUZZ")
        else:
            print(i)
try:
    a=int(input("Sonni kiriting 1 dan 9 gacha :"))
    b=int(input("Boshqa sonni kiriting 1 dan 9 gacha :"))
    if not (1 <= a <= 9 and 1 <= b <= 9):
        raise ValueError("Kiritilgan qiymat 1 va 9 oralig'ida emas")
    if a == b:
        raise ValueError("sonlar turlicha bo'lishi kerak")
except ValueError as xato:
    print(f"Xatolik mavjud:{xato}")
else:
    chiqar(a,b)

