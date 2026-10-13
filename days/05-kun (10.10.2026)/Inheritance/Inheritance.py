# G’oya: bola klass otaning kodini qayta yozmasdan oladi va faqat farqini qo’shadi.
#
# Shart:
#
# Xodim(ism, oylik): ism bo’sh yoki oylik <= 0 bo’lsa ValueError. oylik_hisobla() oyligini qaytaradi. malumot() "Ali, oylik: 5 000 000" ko’rinishidagi matn qaytaradi.
# Dasturchi(Xodim): qo’shimcha loyihalar (soni, int). oylik_hisobla(): oylik + har loyiha uchun 200 000.
# Menejer(Xodim): qo’shimcha jamoa (ro’yxat, __init__ ichida yaratilsin). jamoaga_qosh(xodim) (faqat Xodim obyekti qabul qilinsin, aks holda TypeError). oylik_hisobla(): oylik + jamoadagi har odam uchun 100 000.
# Bola klasslarda __init__ va oylik_hisobla da super() ishlatilsin, otaning kodi takrorlanmasin.
class Xodim:
    def __init__(self, ism, oylik):
        if not isinstance(ism, str) or not ism.strip():
            raise ValueError("Ism bo'sh bo'lishi mumkin emas!")
        if not isinstance(oylik, (int, float)) or oylik <= 0:
            raise ValueError("Oylik musbat son bo'lishi kerak!")
        self.ism=ism
        self.oylik=oylik
    def oylik_hisobla(self):
        return self.oylik
    def malumot(self):
        return f"{self.ism}, oylik: {self.oylik}"

class Dasturchi(Xodim):
    def __init__(self,ism,oylik,loyihasoni):
        super().__init__(ism,oylik)
        if isinstance(loyihasoni,int) and loyihasoni>=0:
            self.loyihasoni=loyihasoni
        else:
            raise ValueError("Loyiha soni butun son bo'lishi kerak!")
    def oylik_hisobla(self):

        return super().oylik_hisobla()+(self.loyihasoni*200000)

class Menejer(Xodim):
    def __init__(self,ism,oylik):
        super().__init__(ism,oylik)
        self.xodimlar=[]
    def jamoaga_qosh(self,xodim):
        if not isinstance(xodim,Xodim):
            raise TypeError("Bu obyekt Xodim classiga tegishli emas ")
        self.xodimlar.append(xodim)

    def oylik_hisobla(self):
        return super().oylik_hisobla()+(len(self.xodimlar)*100000)
    def xodimlar_malumotlari(self):
        for x in self.xodimlar:
            print(x.malumot())