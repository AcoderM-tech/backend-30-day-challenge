from datetime import date, timedelta
from pathlib import Path

asosiy = Path("days")
asosiy.mkdir(exist_ok=True)

kun = date.today() + timedelta(days=1)  # ertangi kundan boshlanadi
raqam = 1

while raqam <= 30:
    if kun.weekday() != 6:  # yakshanba o'tkazib yuboriladi
        papka = asosiy / f"{raqam:02d}-kun ({kun.strftime('%d.%m.%Y')})"
        papka.mkdir(exist_ok=True)
        (papka / ".gitkeep").touch()  # Git bo'sh papkani saqlamaydi
        print(papka)
        raqam += 1
    kun += timedelta(days=1)