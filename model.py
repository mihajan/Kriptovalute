#uvozim knjižnico ki mi bo pomagala pri pridobivanju podatkov trenutnih cen iz interneta
from yahoofinancials import YahooFinancials


class Model:
    def __init__(self):
        self.portfelji = []
        self.aktualni_portfelj = None

    def dodaj_portfelj(self, portfelj):
        self.portfelji.append(portfelj)
        if not self.aktualni_portfelj:
            aktualni_portfelj = portfelj

    def pobrisi_portfelj(self, portfelj):
        self.portfelji.remove(portfelj)

    def zamenjaj_portfelj(self, portfelj):
        self.aktualni_portfelj = portfelj

    def stevilo_razlicnih_portfeljev(self):
        return len(self.portfelji)

    def dodaj_kovanec(self, kovanec): #poskrbi da se kovanec doda na aktivni portfelj
        self.aktualni_portfelj.dodaj_kovanec(kovanec)

    def prodaj_kovanec(self, kovanec): 
        """Odstrani kovanec iz portfelja. Kot bi npr. nekaj kupil"""
        self.aktualni_portfelj.kovanci.remove(kovanec)

    def vrednost_vseh_portfeljev_modela(self):
        skupaj = 0
        for portfelj in self.portfelji:
            skupaj += portfelj.vrednost_portfelja()
        return skupaj

class Portfelj:
    def __init__(self, ime):
        self.ime = ime
        self.kovanci = []  #v ta seznam se bodo appendali kovanci ki jih bomo želeli dodati na portfelj

    def dodaj_kovanec(self, kovanec):
        self.kovanci.append(kovanec)

    def stevilo_razlicnih_kovancev(self):
        return len(self.kovanci)

    def vrednost_portfelja(self):
        vrednost = 0
        for kovanec in self.kovanci:
            vrednost += kovanec.trenutna_vrednost_dolocenega_kovanca()
        return vrednost
    


class Kovanec:
    def __init__(self, kratica, polno_ime, posebnost, kolicina):
        self.kratica = kratica
        self.polno_ime = polno_ime
        self.posebnost = posebnost
        self.kolicina = kolicina
        

    def __str__(self):
        return f'{self.polno_ime} je vrsta kriptovalute z uradno kratico {self.kratica}, katere imaš v lasti {self.kolicina} enot.'

    def __repr__(self):
        return f'Kovanec({self.kratica}, {self.polno_ime}, {self.posebnost}, {self.kolicina})'


    def trenutna_cena_enega(self):      
        return YahooFinancials(f'{self.kratica}-USD').get_current_price()        
            
    def trenutna_vrednost_dolocenega_kovanca(self):
            return float(self.kolicina) * self.trenutna_cena_enega()






