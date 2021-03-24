import json

libri = {
    "libro1" : {"titolo":"narnia", "autore":"io", "genere":"fantasy"},
    "libro2" : {"titolo2":"narnia2", "autore2":"io2", "genere2":"fantasy2"},
    "libro3" : {"titolo3":"narnia3", "autore3":"io3", "genere3":"fantasy3"},
    "libro4" : {"titolo4":"narnia4", "autore3":"io4", "genere4":"fantasy4"},
    "libro5" : {"titolo5":"narnia5", "autore3":"io5", "genere5":"fantasy5"},
    "libro6" : {"titolo6":"narnia6", "autore3":"io6", "genere6":"fantasy6"},
    "libro7" : {"titolo7":"narnia7", "autore3":"io7", "genere7":"fantasy7"},
    "libro8" : {"titolo8":"narnia8", "autore3":"io8", "genere8":"fantasy8"},
    "libro9" : {"titolo9":"narnia9", "autore3":"io9", "genere9":"fantasy9"},
    "libro10" : {"titolo10":"narnia10", "autore3":"io10", "genere10":"fantasy10"}
}

with open("libri.json", "w") as L:
    json.dump(libri, L)

L.close()

with open("libri.json", "r") as L:
    dati = json.load(L)

L.close()

print(dati)