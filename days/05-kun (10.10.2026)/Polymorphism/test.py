from Polymorphism import *
def xato_beradimi(funksiya, *args):
    try:
        funksiya(*args)
    except (ValueError, TypeError, NotImplementedError):
        return True
    return False
assert konsert([Mushuk(), It(), Qush()]) == ["Miyov", "Vov", "Chirq"]
# assert konsert([Robot(), It()]) == ["Bip-bip", "Vov"]
assert konsert([]) == []
assert xato_beradimi(konsert, [Mushuk(), 5])

class Buzuq:
    def ovoz(self): return self.yoq

try:
    konsert([Buzuq()])
except AttributeError:
    pass            # to'g'ri: haqiqiy xato yashirilmadi
except TypeError:
    raise AssertionError("Buzuq xatosi 'ovoz bera olmaydi' deb yashirildi")

assert It().harakat() == "yuguradi"
assert Qush().harakat() == "uchadi"