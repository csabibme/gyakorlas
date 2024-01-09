class Etel:
    def __init__(self, nev, ar):
        self.nev = nev
        self.ar = ar

class Etterem:
    def __init__(self, etteremnev, menuelemek):
        self.etteremnev = etteremnev
        self.menuelemek = menuelemek

    def __str__(self):
        return f"Az étterem neve: {self.etteremnev}"

    def __add__(self, other):
        self.menuelemek.append(other)

    def getmenuitems(self):
        for menuitem in self.menuelemek:
            print (f"{menuitem.nev} .......... {menuitem.ar}")

etel1 = Etel("Krumplistészta", 899)
etel2 = Etel("Pacalprökölt", 1500)
my_menu = [etel1, etel2]

azetterem = Etterem("Bográcsos Hely", my_menu)

for i in range(2):
    etel_neve = input("Az étel neve: ")
    etel_ara = int(input("Az étel ára: "))
    if etel_ara < 0 or etel_ara > 100000:
        print("Nem megfelelő ár!")
    else:
        azetterem + Etel(etel_neve, etel_ara)


my_etel = Etel("Gulyástanya", 1250)
print(azetterem)
azetterem.getmenuitems()