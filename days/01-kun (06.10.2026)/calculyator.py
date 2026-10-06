def qosh(a,b):
    return a+b
def ayir(a,b):
    return a-b
def kopaytir(a,b):
    return a*b
def qoldiq(a, b):
    if b == 0:
        raise ValueError("0 ga bo'lib bo'lmaydi")
    return a % b
def daraja(a,b):
    return a**b
def bol(a, b):
    if b == 0:
        raise ValueError("0 ga bo'lib bo'lmaydi")
    return a / b
def son_ol(matn):
    while True:
        try:
            return float(input(matn))
        except ValueError:
            print("Xato: faqat son kiriting")
amallar={
    "+":qosh,
    "-":ayir,
    "*":kopaytir,
    "/":bol,
    "^":daraja,
    "%":qoldiq
}
def amal_ol():
    while True:
        belgi = input(f"Amal kiriting ro'yxatdan ixtiyoriysini ({' '.join(amallar)}): ").strip()
        if belgi in amallar:
            return belgi
        print("Xato: bunday amal yo'q")

def main():
    while True:
        a = son_ol("1-sonni kiriting: ")
        belgi = amal_ol()
        b = son_ol("2-sonni kiriting: ")

        try:
            natija = amallar[belgi](a, b)
        except ValueError as xato:
            print(f"Xato: {xato}")
        else:
            print(f"Natija: {a:g} {belgi} {b:g} = {natija:g}")

        javob = input("Yana hisoblaymizmi? (ha/yo'q): ").strip().lower()
        if javob != "ha":
            print("Xayr!")
            break


if __name__ == "__main__":
    main()







