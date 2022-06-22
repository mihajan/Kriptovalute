import bottle
from model import Model, Portfelj, Kovanec

IME_DATOTEKE = "stanje.json"
try:
    testni_model = Model.preberi_iz_datoteke(IME_DATOTEKE)
except FileNotFoundError:
    testni_model = Model()
#testni_model = Model()

@bottle.get("/navodila/")
def testna_stran():
    return bottle.template("navodila.tpl")



@bottle.get("/")
def osnovni_meni():
    return bottle.template(
        "osnovni-meni.tpl",
        stevilo_portfeljev=testni_model.stevilo_razlicnih_portfeljev(),
        portfelji = testni_model.portfelji
    )
    
@bottle.get("/portfelj/<id_portfelja:int>/")
def pokazi_portfelj(id_portfelja):
    portfelj = testni_model.portfelji[id_portfelja]
    return bottle.template(
        "portfelj.tpl",
        id_portfelja=id_portfelja,
        portfelj=portfelj
    )

@bottle.post("/dodaj-kovanec/<id_portfelja:int>/")
def dodaj_kovanec(id_portfelja):
    portfelj = testni_model.portfelji[id_portfelja]
    kratica = bottle.request.forms.getunicode("kratica")
    polno_ime = bottle.request.forms.getunicode("polno_ime")
    posebnost = bottle.request.forms.getunicode("posebnost")
    kolicina = bottle.request.forms.getunicode("kolicina")
    kovanec = Kovanec(kratica, polno_ime, posebnost, kolicina)
    portfelj.dodaj_kovanec(kovanec)
    bottle.redirect("/")




   













bottle.run(reloader=True, debug=True)