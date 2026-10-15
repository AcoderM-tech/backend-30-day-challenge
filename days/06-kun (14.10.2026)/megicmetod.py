class Pul:

    def __init__(self,miqdor,valyuta):
        if not isinstance(miqdor,(int,float)):
            raise TypeError("Miqdor son bo'lishi kerak!!")
        self.miqdor = miqdor
        self.valyuta = valyuta

    def __str__(self):
        return f"{self.miqdor} {self.valyuta}"
    def __eq__(self,ob2):
        if not isinstance(ob2,Pul):
            classnomi=self.__class__.__name__
            raise TypeError(f"Kirilgan obyekt {classnomi} classi obyekti bo'lishi kerak!!")
        if self.valyuta != ob2.valyuta:
            return False
        return True
    def __add__(self,ob1):
        if not isinstance(ob1,Pul):
            classnomi=self.__class__.__name__
            raise TypeError(f"Kirilgan obyekt {classnomi} classi obyekti bo'lishi kerak!!")
        if self.__eq__(ob1)==False:
            raise ValueError("Ikki xil valyutani qo'shib bo'midi!")
        return ob1.miqdor+self.miqdor

