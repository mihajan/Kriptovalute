from model import Model, Portfelj, Kovanec

testni_model = Model()

DODAJ_PORTFELJ = 1
POBRISI_PORTFELJ = 2
ZAMENJAJ_PORTFELJ = 3
DODAJ_KOVANEC = 4
PRODAJ_KOVANEC = 5
PRIKAZI_POSAMEZNE_KOVANCE = 6
IZHOD = 7

def prikaz_portfelja(portfelj):
    st_kovancev = portfelj.stevilo_razlicnih_kovancev()
    return f"Na portfelju {portfelj.ime.upper()} je {st_kovancev} kovancev"


def prikaz_kovanca(kovanec):
    return f'{self.polno_ime} ({self.kratica})- si lastiš {self.kolicina} enot.'


def izberi_moznost(moznosti):
    '''Uporabniku našteje možnosti ter vrne izbrano. !skopirana koda iz datoteke iz predavanj!'''
    for i, (_moznost, opis) in enumerate(moznosti, 1):
        print(f'{i}) {opis}')
    while True:
        i = preberi_stevilo()
        if 1 <= i <= len(moznosti):
            moznost, _opis = moznosti[i - 1]
            return moznost
        else:
            print(f'Vnesti morate število med 1 in {len(moznosti)}.')    

def preberi_stevilo():
    '''iz konzole prebere vpisnao število, v naspotnem primeru javi napako'''
    while True:
        vnos = input('> ')
        try:
            return int(vnos)
        except ValueError:
            print('Vnesti morate število.')

def izberi_aktivni_portfelj(model):
    return izberi_moznost([(portfelj, prikaz_portfelja(portfelj)) for portfelj in model.portfelji])

def izberi_kovanec(model):
    '''Funkcija ki pomaga pri izbiri kovanca da ga bom lahko izbrisal'''
    return izberi_moznost([kovanec, prikaz_kovanca(kovanec) for kovanec in model.aktualni_portfelj.kovanci])
    
def prikazi_aktualne_kovance():
    pass

def tekstovni_vmesnik():
    uvodni_pozdrav()
    while True:
        pokazi_portfelje()
        pokazi_skupno_vrednost_portfeljev()
        print("\n Vpiši ustrezno število pred željeno aktivnostjo: ")
        izbran_ukaz = izberi_moznost([
            (DODAJ_PORTFELJ, "ustvari nov portfelj"),
            (POBRISI_PORTFELJ, "pobriši portfelj"),
            (ZAMENJAJ_PORTFELJ, "prikaži drug portfelj"),
            (DODAJ_KOVANEC, "dodaj nov kovanec na portfelj"),
            (PRODAJ_KOVANEC, "odstrani kovanec iz portfelja"),
            (PRIKAZI_POSAMEZNE_KOVANCE, "prikaži vse kovance"),
            (IZHOD, "zaključi z izvajanjem programa")
        ])
        if izbran_ukaz == DODAJ_PORTFELJ:
            dodaj_portfelj()
        elif izbran_ukaz == POBRISI_PORTFELJ:
            pobrisi_portfelj()  
        elif izbran_ukaz == ZAMENJAJ_PORTFELJ:
            zamenjaj_portfelj()
        elif izbran_ukaz == DODAJ_KOVANEC:
            dodaj_kovanec()
        elif izbran_ukaz == PRODAJ_KOVANEC:
            prodaj_kovanec()
        elif izbran_ukaz == PRIKAZI_POSAMEZNE_KOVANCE:
            prikazi_posamezne_kovance()
        elif izbran_ukaz == IZHOD:
            pozdrav_v_slovo()
            break
        



def uvodni_pozdrav():
    print("Pozdravljen v programu kjer lahko spremljaš vrednosti svojih kriptovalut!")

def pozdrav_v_slovo():
    print("Lepo se imej, nasviednje!")

def dodaj_portfelj():
    print("Vnesite zahtevane podatke portfelja.")
    ime = input("ime> ")
    nov_portfelj = Portfelj(ime)
    testni_model.dodaj_portfelj(nov_portfelj)

def pobrisi_portfelj():
    print("Izberi številko pred portfeljem, ki ga želiš izbrisati:")
    portfelj = izberi_aktivni_portfelj(testni_model)
    testni_model.pobrisi_portfelj(portfelj)

def zamenjaj_portfelj():
    print("Izberi željeni aktivni portfelj.")
    portfelj = izberi_aktivni_portfelj(testni_model)
    testni_model.zamenjaj_portfelj(portfelj)

def dodaj_kovanec():
    print("Vnesite podatke za nov kovanec:")
    kratica = input("Kratica> ")
    polno_ime = input("Ime> ")
    posebnost = input("Posebnost> ")
    kolicina = input("Količina v lasti> ")
    nov_kovanec = Kovanec(kratica, polno_ime, posebnost, kolicina)
    testni_model.dodaj_kovanec(nov_kovanec)

def prodaj_kovanec():
    print("Izberite kovanec, ki ga želite odstraniti:")
    kovanec = izb

def pokazi_portfelje():
    '''Prikaže imena portfeljev v modelu in njihove vrednosti'''
    for portfelj in testni_model.portfelji:
        print(f'-{portfelj.ime.capitalize()}: {round(portfelj.vrednost_portfelja(), 2)}$')

def pokazi_skupno_vrednost_portfeljev():
    print(f'Skupna vrednost tvojih portfeljev je: {round(testni_model.vrednost_vseh_portfeljev_modela(), 2)}$')








tekstovni_vmesnik()
#----------------------------------------------------------------------------------------
def osnovni_zaslon(): #ta funkcija je neuporabna
    print('Kaj bi rad počel?')
    print('1) Preveril vrednosti portfeljev?')
    print('2) Pogledal posamezne kovance iz portfelja?')
    print('3) Odstranil kovanec?')
    vnos = input('> ')
    if vnos == '1': 
        pass
               
    elif vnos == '2':
        pokazi_posamezne_kovance()
    elif vnos == '3':
        pass   


holding = Portfelj('holding')
trading = Portfelj('trading')
testni_model.dodaj_portfelj(holding)
testni_model.dodaj_portfelj(trading)
ethereum = Kovanec('ETH', 'Ethereum', '', 17.8)
bitcoin = Kovanec('BTC', 'Bitcoin', '', 1.1)
holding.dodaj_kovanec(bitcoin)
trading.dodaj_kovanec(ethereum)