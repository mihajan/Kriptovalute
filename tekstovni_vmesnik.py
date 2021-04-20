from model import Model, Portfelj, Kovanec

testni_model = Model()
holding = Portfelj('holding')
trading = Portfelj('trading')
testni_model.dodaj_portfelj(holding)
testni_model.dodaj_portfelj(trading)
ethereum = Kovanec('ETH', 'Ethereum', '', 17.8)
bitcoin = Kovanec('BTC', 'Bitcoin', '', 1.1)
holding.dodaj_kovanec(bitcoin)
trading.dodaj_kovanec(ethereum)




def tekstovni_vmesnik():
    uvodni_pozdrav()
    while True:
        osnovni_zaslon()


def uvodni_pozdrav():
    print("Pozdravljen v programu kjer lahko spremljaš vrednosti svoji kriptovalut!")

def osnovni_zaslon():
    print('Kaj bi rad počel?')
    print('1) Preveril vrednosti portfeljev?')
    print('2) Pogledal posamezne kovance iz portfelja?')
    print('3) Odstranil kovanec?')
    vnos = input('> ')
    if vnos == '1':  #ne deluje kot bi moral? ne izpiše obeh funkcij naenkrar, vsako posebej pa
        pokazi_portfelje()
        pokazi_skupno_vrednost_portfeljev()       
    elif vnos == '2':
        pokazi_posamezne_kovance()
    elif vnos == '3':
        pass



def pokazi_portfelje():
    for portfelj in testni_model.portfelji:
        print(f'-{portfelj.ime.capitalize()}: {round(portfelj.vrednost_portfelja(), 2)}$')

def pokazi_skupno_vrednost_portfeljev():
    print(f'Skupna vrednost tvojih portfeljev je: {round(testni_model.vrednost_vseh_portfeljev_modela(), 2)}')

def pokazi_posamezne_kovance():
    vnos = input('Kovance katerega portfelja želiš videti? (vpiši ime) > ')
    # v modelu naredi funkcijo spisek kovancev ki jo bo to vrnilo
    pass
    




#lahko bi dodal še funkcijo ki prikaže skupno vrednost vseh portfelejv, ki prikaže vse kovance in njihovi vrednosti


tekstovni_vmesnik()
        