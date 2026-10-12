# 📅 Day 5: Ob’yektga yo’naltirilgan dasturlash (OOP) va Asosiy Tamoyillar

Bugun Python'da **Ob’yektga yo’naltirilgan dasturlash (OOP)**ning 4 ta asosiy fundamental tamoyili — Inqapsulatsiya (Encapsulation), Vorislik (Inheritance), Polimorfizm (Polymorphism) va Abstraksiya (Abstraction) bo'yicha to'liq amaliyot bajardim. Har bir tamoyil bo'yicha alohida modellar va ularni to'liq tekshiruvchi avtomatlashtirilgan testlar yozildi.

## 🚀 Bugun O'rganilgan Konseptlar

* **Inqapsulatsiya (Encapsulation):** Ma'lumotlarni tashqi ta'sirdan yashirish (`__atribut`), validatsiya qoidalari va xavfsizlik mexanizmlari (masalan, 3 marta noto'g'ri kod kiritilganda bloklanadigan Seyf klassi).
* **Vorislik (Inheritance):** Ota klass (`super()`) kodlarini takrorlamagan holda bola klasslarga meros qilib berish va ularga maxsus xususiyatlar qo'shish (Xodim, Dasturchi va Menejer ierarxiyasi).
* **Polymorphism (Polymorphism):** Turli xil klassdagi obyektlarning bir xil nomdagi metodlar orqali turlicha harakat qilishi, `isinstance` tekshiruvlarisiz umumiy interfeysda ishlash va xatolarni `try/except` yordamida ushlash.
* **Abstraksiya (Abstraction):** Umumiy interfeysni belgilab beruvchi `NotImplementedError` orqali ota klassni yaratish va aniq tafsilotlarni bola klasslarda to'ldirish (To'lov tizimlari: Naqd, Karta, Komissiyali).

---

## 🛠️ Bajarilgan Amaliy Masalalar va Testlar

### 1. Inqapsulatsiya (`Encapsulation/`)
* **`Encapsulation.py`**: 4 xonali matnli kod va musbat balansni talab qiluvchi, shuningdek ketma-ket 3 marta noto'g'ri kod kiritilsa bloklanadigan `Seyf` klassi.
* **`test.py`**: Seyfning barcha validatsiya qoidalari, pul qo'shish, yechish va bloklanish holatlarini tekshiruvchi testlar.

### 2. Vorislik (`Inheritance/`)
* **`Inheritance.py`**: `Xodim` ota klassi va uning bazasida ishlaydigan loyihalar soniga qarab oylik hisoblaydigan `Dasturchi` hamda jamoa boshqaruviga ega `Menejer` klasslari (`super()` yordamida).
* **`test.py`**: Xodimlar, dasturchilar va menejerlarning maoshlarini hisoblash hamda tip tekshiruvlarini tekshiruvchi testlar.

### 3. Polimorfizm (`Polymorphism/`)
* **`Polymorphism.py`**: Ota klassi bo'lmagan, lekin bir xil `ovoz()` va `harakat()` metodlariga ega `Mushuk`, `It`, `Qush` va `Robot` klasslari. `konsert` funksiyasi orqali ularni turini tekshirmasdan boshqarish va `AttributeError` ni `TypeError` ga o'zgartirish.
* **`test.py`**: Konsert funksiyasining ishlashi va noto'g'ri obyekt berilganda xatolarni ushlashini tekshiruvchi testlar.

### 4. Abstraksiya (`Abstraction/`)
* **`Abstraction.py`**: `Tolov` ota klassi (`NotImplementedError` bilan) va uning mantiqini davom ettiruvchi `Naqd`, `Karta`, hamda `Komissiyali` to'lov turlari.
* **`test.py`**: Turli to'lov usullarini va komissiya hisoblash jarayonlarini tekshiruvchi testlar.

---

## 📂 Kunlik Kodlar strukturasi

```
05-kun (10.10.2026)/
├── Abstraction/
│   ├── Abstraction.py   # To'lov tizimlari abstraksiya mantiqi
│   └── test.py          # Abstraksiya testlari
├── Encapsulation/
│   ├── Encapsulation.py # Seyf klassi va inqapsulatsiya
│   └── test.py          # Seyf xavfsizlik testlari
├── Inheritance/
│   ├── Inheritance.py   # Xodim, Dasturchi va Menejer ierarxiyasi
│   └── test.py          # Vorislik testlari
└── Polymorphism/
    ├── Polymorphism.py  # Polimorfizm va konsert funksiyasi
    └── test.py          # Polimorfizm testlari
```

## ⏭️ Keyingi qadam

Obyektga yo'naltirilgan dasturlash (OOP) tamoyillarini to'liq yakunlab, keyingi bosqichda ma'lumotlar bazasi (Database) va SQL bilan ishlashga o'tamiz.