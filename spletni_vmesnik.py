import bottle
from model import Model, Portfelj, Kovanec

IME_DATOTEKE = "stanje.json"
try:
    testni_model = Model.preberi_iz_datoteke(IME_DATOTEKE)
except FileNotFoundError:
    testni_model = Model()


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




bottle.run(reloader=True, debug=True)