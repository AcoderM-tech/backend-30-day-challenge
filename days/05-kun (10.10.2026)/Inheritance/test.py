from Inheritance import Xodim, Dasturchi, Menejer

try:
    x1 = Xodim("Ali", 5000000)
    print(x1.malumot())
    print("Oylik:", x1.oylik_hisobla())
except Exception as e:
    print("Xato:", e)

try:
    d1 = Dasturchi("Vali", 6000000, 3)
    print(d1.malumot())
    print("Dasturchi oyligi:", d1.oylik_hisobla())
except Exception as e:
    print("Xato:", e)

try:
    m1 = Menejer("Hasan", 8000000)
    m1.jamoaga_qosh(x1)
    m1.jamoaga_qosh(d1)
    print(m1.malumot())
    print("Menejer oyligi:", m1.oylik_hisobla())
except Exception as e:
    print("Xato:", e)

try:
    m1.jamoaga_qosh("Oddiy matn")
except TypeError as e:
    print("Kutilgan TypeError:", e)
except Exception as e:
    print("Boshqa xato:", e)

try:
    x_xato = Xodim("", -100)
except ValueError as e:
    print("Kutilgan ValueError:", e)