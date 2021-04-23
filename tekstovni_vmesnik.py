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
    return f'{kovanec.polno_ime} ({kovanec.kratica})- si lastiš {kovanec.kolicina} enot.'




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
    return izberi_moznost([(kovanec, prikaz_kovanca(kovanec)) for kovanec in model.aktualni_portfelj.kovanci])
    


def tekstovni_vmesnik():
    uvodni_pozdrav()
    while True:
        stevilo_razlicnih_portfeljev()
        #pokazi_portfelje()
        #pokazi_skupno_vrednost_portfeljev()
        print("\nVpišite številko pred dejavnostjo, ki jo želite narediti.")
        izbran_ukaz = izberi_moznost([
            (DODAJ_PORTFELJ, "ustvari nov portfelj"),
            (POBRISI_PORTFELJ, "pobriši portfelj"),
            (ZAMENJAJ_PORTFELJ, "prikaži drug portfelj"),
            (DODAJ_KOVANEC, "dodaj kovanec na aktivni portfelj"),
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
            pokazi_posamezne_kovance()
        elif izbran_ukaz == IZHOD:
            pozdrav_v_slovo()
            break
        



def uvodni_pozdrav():
    print("Pozdravljen v programu kjer lahko spremljaš trenutne vrednosti svojih kriptovalut!")
    print("----------------------------------------------------------------------------------")

def pozdrav_v_slovo():
    print("Lepo se imej, nasviednje!")

def stevilo_razlicnih_portfeljev():
    if testni_model.stevilo_razlicnih_portfeljev() != 0:
        print(f"\nTreutno imate toliko portfeljev: {testni_model.stevilo_razlicnih_portfeljev()}")
        print(f"Vaš trenutno aktiven portfelj je: {testni_model.aktualni_portfelj}")
    else:    
        print("Ustvarjenega nimate še nobenega portfelja, zato si ga prosim najprej ustvarite.\n")
        dodaj_portfelj()
   
        

def pokazi_portfelje():
    '''Prikaže imena portfeljev v modelu in njihove vrednosti'''
    for portfelj in testni_model.portfelji:
        print(f'-{portfelj.ime.capitalize()}: {round(portfelj.vrednost_portfelja(), 2)}$')

def pokazi_skupno_vrednost_portfeljev():
    print(f'Skupna vrednost tvojih portfeljev je: {round(testni_model.vrednost_vseh_portfeljev_modela(), 2)}$')

def dodaj_portfelj():
    print("Vpišite kako želite, da se vaš portfelj imenuje.")
    ime = input("ime> ")
    nov_portfelj = Portfelj(ime)
    testni_model.dodaj_portfelj(nov_portfelj)
    #ko ustvarimo nov portfelj ta postane aktualni
    testni_model.aktualni_portfelj = nov_portfelj

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
    kovanec = izberi_kovanec(testni_model)
    testni_model.prodaj_kovanec(kovanec)

def pokazi_posamezne_kovance():
    '''Prikaže kovance na aktualnem portfelju'''
    print("IME -- KRATICA -- ŠT ENOT V LASTI")
    for kovanec in testni_model.aktualni_portfelj.kovanci:
        print(f"-{prikaz_kovanca(kovanec)}")


    










tekstovni_vmesnik()
#----------------------------------------------------------------------------------------


