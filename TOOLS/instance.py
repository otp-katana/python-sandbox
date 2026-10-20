"""
üsalma = lambda x: pow(x, 5)
print(üsalma(4))

üsalma = lambda x, y: pow(x, y)
print(üsalma(2, 8))

çarpma = lambda x, y: x * y
print(çarpma(5, 7), type(çarpma))

a = [1, 2, 3, 4, 5]
b = ["a", "b", "c", "d", "e"]

zıpır = dict(zip(a, b))
print(zıpır, type(zıpır))


print(dict(zip(a,b)))


liste = [i**2 for i in range(10)]
print(liste)

küme = {i**2 for i in range(10) if i > 5}
print(küme, type(küme))

sözlük = {i+1: i*2 for i in range(5)}
print(sözlük, type(sözlük))
"""
"""
class köpek:
    pass
"""

class köpek():
    def __init__(self, isim, yaş):
        self.isim = isim
        self.yaş = yaş

felix = köpek("Felix", 3)
fox = köpek("Fox", 2)
küheylan = köpek(42, 5)
"""
print(felix.isim)
print(felix.yaş)
"""

felix.isim = "Max"

print(felix.isim)



class hayvan():
    def __init__(self, isim, yaş, tür, ırk):
        self.isim = isim
        self.yaş = yaş
        self.tür = tür
        self.ırk = ırk
        pass

a = hayvan("Küheylan", 3, "Köpek", "Golden Retreiver")
b = hayvan("Bızdık", 7, "Kedi", "Maine Coon")
c = hayvan("Abuzer", 4, "Kedi", "Maine Coon")

print(a.ırk)


class x():
    def __init__(self, a, b, c, d, f):
        self.a = a
        self.b = b
        pass