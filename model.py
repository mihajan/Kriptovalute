#knjižnica yahoofinancials služi za pridobivanje aktualnih cen
from yahoofinancials import YahooFinancials 
import json

class Model:
    def __init__(self):
        self.portfelji = []
        self.aktualni_portfelj = None

    def dodaj_portfelj(self, portfelj):
        self.portfelji.append(portfelj)
        if not self.aktualni_portfelj: #če nimamo še nobenega portfelja to postane tisti ki ga dodajamo
            aktualni_portfelj = portfelj

    def pobrisi_portfelj(self, portfelj):
        self.portfelji.remove(portfelj)

    def zamenjaj_portfelj(self, portfelj):
        self.aktualni_portfelj = portfelj

    def stevilo_razlicnih_portfeljev(self):
        return len(self.portfelji)

    def dodaj_kovanec(self, kovanec):
        """poskrbi da se kovanec doda na aktivni portfelj"""
        self.aktualni_portfelj.dodaj_kovanec(kovanec)

    def prodaj_kovanec(self, kovanec): 
        """Odstrani kovanec iz portfelja. Kot bi npr. nekaj kupil"""
        self.aktualni_portfelj.kovanci.remove(kovanec)

    def vrednost_vseh_portfeljev_modela(self):
        skupaj = 0
        for portfelj in self.portfelji:
            skupaj += portfelj.vrednost_portfelja()
        return skupaj

    def v_slovar(self):
        return {
            "portfelji": [portfelj.v_slovar() for portfelj in self.portfelji],
            "aktualni_portfelj": self.portfelji.index(self.aktualni_portfelj)
            if self.aktualni_portfelj
            else None,
        }

    @staticmethod
    def iz_slovarja(slovar):
        model = Model()
        model.portfelji = [Portfelj.iz_slovarja(sl_portfelja) for sl_portfelja in slovar["portfelji"]]
        if slovar["aktualni_portfelj"] is not None:
            model.aktualni_portfelj = model.portfelji[slovar["aktualni_portfelj"]]
        return model

    def shrani_v_datoteko(self, ime_datoteke):
        with open(ime_datoteke, "w", encoding="UTF-8") as dat:
            slovar = self.v_slovar()
            json.dump(slovar, dat)

    @staticmethod
    def preberi_iz_datoteke(ime_datoteke):
        with open(ime_datoteke) as dat:
            slovar = json.load(dat)
            return Model.iz_slovarja(slovar)

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

    def v_slovar(self):
        return {
            "ime": self.ime,
            "kovanci": [kovanec.v_slovar() for kovanec in self.kovanci],
        }
    
    @staticmethod
    def iz_slovarja(slovar):
        portfelj = Portfelj(slovar["ime"])
        portfelj.kovanci = [
            Kovanec.iz_slovarja(sl_kovanci) for sl_kovanci in slovar["kovanci"]
        ]
        return portfelj


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
        return round(YahooFinancials(f'{self.kratica}-USD').get_current_price(), 2)        
            
    def trenutna_vrednost_dolocenega_kovanca(self):
        return round(float(self.kolicina) * self.trenutna_cena_enega(), 2)

    def v_slovar(self):
        return {
            "kratica": self.kratica,
            "polno_ime": self.polno_ime,
            "posebnost": self.posebnost,
            "kolicina": self.kolicina,
        }

    @staticmethod
    def iz_slovarja(slovar):
        return Kovanec(
            slovar["kratica"],
            slovar["polno_ime"],
            slovar["posebnost"],
            slovar["kolicina"],
        )




