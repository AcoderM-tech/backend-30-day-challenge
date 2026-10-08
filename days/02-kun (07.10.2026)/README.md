# 📅 Day 2: Python Lists & Algorithmic Challenges

Bugun Python dasturlash tilida **Lists (Roʻyxatlar)** maʼlumot turining oʻziga xos xususiyatlari, xotirada ishlash mexanizmlari, maxsus metodlari va murakkab algoritmlar ustida ishladim.

## 🚀 Bugun O'rganilgan Konseptlar

* **Ma'lumot turlari farqi:** `list`, `tuple`, `dict` va `set` tuzilmalarining mantiqiy hamda arxitekturaviy farqlari.
* **Xotira boshqaruvi (Memory Management):** `b = a` (havola berish) va `b = a.copy()` (yangi nusxa olish) operatorlarining farqlari hamda ularning o'zgaruvchan (mutable) turlarga ta'siri.
* **List Comprehension:** Shartli va tsiklli amallarni bitta qatorda ixcham yozish.
* **Two Pointers texnikasi:** Elementlarni xotirada ortiqcha surishlarsiz (O(n) vaqt unumdorligida) indekslar yordamida joyida (in-place) almashtirish.

---

## 🛠 Bajarilgan Amaliy Masalalar

### 1. Elementlarni hisoblash va indekslarni aniqlash
Ro'yxat ichidan berilgan qiymat necha marta qatnashgani va uning joylashgan indekslarini `enumerate()` yordamida aniqlash.

### 2. Dublikatlardan tozalash (Set-siz)
Asl ro'yxat elementlarining kiritilish tartibini saqlagan holda, takrorlangan qiymatlarni `set` ishlatmasdan tozalash algoritmi.

### 3. Shartli List Comprehension
1 dan 50 gacha bo'lgan sonlar ichidan faqat 3 ga bo'linadiganlarining kvadratlaridan iborat yangi ro'yxatni bir qator kod bilan shakllantirish.

### 4. Aylanma surish (Rotate List)
Ro'yxat elementlarini xotirada yangi joy ochmasdan (`in-place`), slicing yordamida o'ngga `k` marta samarali surish algoritmi.

### 5. Nollarni oxiriga surish (Move Zeroes)
`Two Pointers` strategiyasi asosida ro'yxatdagi nollarni saqlangan tartibni buzmagan holda bitta tsiklda eng oxiriga ko'chirish.

### 6. Aksiyalardan maksimal foyda (Best Time to Buy and Sell Stock)
Kunlik aksiyalar narxidan kelib chiqib, minimal narxni eslab qolish orqali bitta urinishda (O(n) dynamic approach) eng katta foydani hisoblash.

---

## 💻 Kunlik Kodlar strukturasi

Bugungi mashqlar va ularning optimal yechimlari `02-kun/list.py` fayliga joylandi.
