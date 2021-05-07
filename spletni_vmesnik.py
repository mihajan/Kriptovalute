import bottle
from model import Model, Portfelj, Kovanec

#IME_DATOTEKE = "stanje.json"
#try:
#    testni_model = Model.preberi_iz_datoteke(IME_DATOTEKE)
#except FileNotFoundError:
testni_model = Model()

@bottle.get("/")
def pozdravna_stran():
    return bottle.template(
        "pozdravna-stran.tpl"
    )


@bottle.post("/osnovni-meni/")
def osnovna_meni():
    return bottle.template(
        "osnovni-meni.tpl",
        stevilo_portfeljev=testni_model.stevilo_razlicnih_portfeljev()
    )
    



bottle.run(reloader=True, debug=True)