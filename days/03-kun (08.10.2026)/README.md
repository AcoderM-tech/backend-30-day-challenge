# 📅 Day 3: Python Dictionaries, Sorting & Advanced Grouping

Bugun Python dasturlash tilida **Dictionaries (Lugʻatlar)** maʼlumot turining oʻziga xos mexanizmlari, xavfsiz qidiruv usullari, qiymatlar boʻyicha saralash va murakkab guruhlash algoritmlari ustida ishladim.

## 🚀 Bugun O'rganilgan Konseptlar

* **Ma'lumotlar strukturasi (Data Structure):** Lugʻatlarning "Kalit — Qiymat" (Key-Value) arxitekturasi va elementlarga kalit orqali murojaat qilish mantiqi.
* **Xavfsiz qidiruv (Crash-safe Access):** `dict[kalit]` yordamida toʻgʻridan-toʻgʻri chaqirish va `.get(kalit, default)` metodi orqali `KeyError` xatoliklarining oldini olish.
* **Ko'zgusimon ob'yektlar (Dict Views):** `.keys()`, `.values()` va `.items()` metodlari qaytaradigan dinamik va unikal obʼyektlarning tabiati.
* **Timsort va Murakkab saralash:** `sorted()` funksiyasining ishlash mexanizmi hamda murakkab tuzilmalarni (kortejlar ro'yxatini) `key` parametri orqali indeks yoki maxsus funksiyalar yordamida qiymat boʻyicha tartiblash.

---

## 🛠️ Bajarilgan Amaliy Masalalar

### 1. Matndagi so'zlar hisoblagichi (`sozlar_soni`)
Uzun matn ichidagi soʻzlarni katta-kichik harflar va tinish belgilaridan (`punctuation`) tozalab, `.get(element, 0) + 1` optimallashgan usuli yordamida bitta tsiklda sanash algoritmi.

### 2. Top-N takrorlangan so'zlar jadvali (`maxsoz`)
Lugʻat elementlarini ularning qiymatlari (soni) boʻyicha `sorted()` yordamida kamayish tartibida saralash hamda natijalarni `f-string` formatlash belgilari (`<` va `>`) orqali konsolga chiroyli va tekis jadval koʻrinishida chiqarish.

### 3. Universal lug'atlarni birlashtirish (`qoshaman`)
Ikkita turli lugʻatni birlashtirish, dabl (bir xil) kalitlar duch kelganda maʼlumot turini (`int` yoki `str`) aniqlab, qiymatlarni oʻchirmasdan oʻzaro matematik yoki matnli qoʻshish (`+`) mexanizmi.

### 4. Aqlli teskari lug'at (`teskari_lugat`)
Lugʻat kalitlari va qiymatlarining oʻrinlarini almashtirish. Qiymatlar takrorlangan (dublikat) holatda, maʼlumotlarni yoʻqotmaslik uchun ularni yangi kalit ostida roʻyxat (`list`) ichiga xavfsiz yigʻish.

### 5. Bosh harflar bo'yicha guruhlash (`guruhlash`)
Berilgan soʻzlar roʻyxatini ularning birinchi harfi boʻyicha guruhlarga ajratib, har bir harfga tegishli soʻzlarni lugʻat ichidagi alohida massivlarga joylashtirish algoritmi.

---

## 📂 Kunlik Kodlar strukturasi

Bugungi lugʻatga oid algoritmik mashqlar va ularning universal, optimal yechimlari `03-kun/dict.py` fayliga joylandi.
