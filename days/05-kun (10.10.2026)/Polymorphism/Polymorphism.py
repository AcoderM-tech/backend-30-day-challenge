class It:
    def ovoz(self):
        return f"Vov"
    def harakat(self):
        return f"yuguradi"
class Mushuk:
    def ovoz(self):
        return f"Miyov"
    def harakat(self):
        print("dumalaydi")
class Qush:
    def ovoz(self):
        return f"Chirq"
    def harakat(self):
        return f"uchadi"
class Robot:
    def ovoz(self):
        return f"Bip bip"
def konsert(royxat):
    standart_turlar = (int, str, float, list, dict, tuple, set, bool)
    ovozlar=[]
    for x in royxat:
        try:
              method=getattr(x,"ovoz",None)
              getattr(method,"__call__")
        except (AttributeError):
              classnomi=x.__class__.__name__
              raise  TypeError(f"{classnomi} klassi obyekti ovoz bera olmaydi!")
        except AssertionError:
             classnomi=x.__class__.__name__
             raise TypeError(f"{classnomi} klassi buzuq ishlamaydi!")
        else:
            ovozlar.append(method())
    return ovozlar
print(konsert([Robot(), Mushuk(), Qush()]))
