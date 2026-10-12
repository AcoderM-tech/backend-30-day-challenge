class Seyf:
    def __init__ (self,kod,ichidagi=0):
        if type(ichidagi) not in [int,float]:
            raise ValueError("Summa must be int or float")
        if type(kod)!=str:
            raise ValueError("Kod must be str")
        kod = kod.strip()
        if len(kod) != 4:
            raise ValueError("Kod 4+ belgili bo'lishi kerak!!")
        if not all(belgi.isdigit() for belgi in kod):
            raise ValueError("Kod to'liq raqamlardan iborat bo'lishi kerak !!")
        if ichidagi < 0:
            raise ValueError("Summa manfiy bo'lishi mumkin emas")
        self.__pul = ichidagi
        self.__kod = kod
        self.__bloklangan = False
        self.__xatolar = 0
    def kod_tekshir(self,kod):
        kod = kod.strip()
        if self.__bloklangan:
           raise ValueError("Bloklangan")
        if kod!=self.__kod:
            self.__xatolar+=1
            if self.__xatolar>=3:
                self.__bloklangan=True
                raise ValueError("Xatolar 3 tadan oshdi va sz bloklandiyiz")
            raise ValueError(f"Kodni xato kiritdiyiz  qolgan urinishlar {3-self.__xatolar}")
        self.__xatolar = 0

    def pul_sol(self,summa):
            if type(summa) not in [int, float]:
                raise ValueError("Summa must be int or float")
            if summa<=0:
                raise ValueError("Manfiy summa kiritib bo'lmaydi")
            self.__pul += summa
            return f"Pul muvaffaqiyatli qo'shildi"

    def pul_ol(self,kod,summa):
        if type(summa) not in [int, float]:
            raise ValueError("Summa must be int or float")
        self.kod_tekshir(kod)
        if summa <= 0:
            raise ValueError("Yechiladigan summa musbat bo'lishi shart!")
        if summa>self.__pul:
            raise ValueError("Hisobingizda mablag' emas !!")
        self.__pul -= summa
        return f"Pul muvaffaqiyatli yechildi"

    def qoldiq(self,kod):
        self.kod_tekshir(kod)
        return self.__pul






