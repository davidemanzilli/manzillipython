class auto:

    # Attributi di Classe
    garanzia = 1
    assicurazione = True
    parcoAuto = 0

    #Metodo costruttore
    def __init__(self,proprietario, marca, modello, cilidrata, cavalli, colore):

        # Attributi di Istanza
        self.proprietario = proprietario
        self.marca = marca
        self.modello = modello
        self.cilindrata = cilidrata
        self.cavalli = cavalli
        self.colore = colore
        
        auto.parcoAuto +=1

    #Metodo di tipo Get
    def scheda(self):
        return f"""
        Scheda 
        proprietario: "{self.proprietario}"
        Marca: {self.marca}
        Modello: {self.modello}
        Cilindrata: {self.cilindrata}
        Cavalli: {self.cavalli}
        colore: {self.colore}
        assicurazione: {self.assicurazione} 
        Garanzia: {auto.garanzia}""" 

    #metodo set | #modifica dei parametri assegnati 
    def modifica_parametri(self):
        scelta = int(input("""
        1 = modifica proprietario
        2 = modifica marca
        3 = modifica modello
        4 = modifica cilindrata
        5 = modifica cavalli
        6 = modifica colore 
        7 = modifica assicurazione 
        8 = modifica garanzia 
        inserisci il numero corrispondente al parametro che vuoi modificare """))
        if scelta == 1:
            nuovo_proprietario = input("inserisci il nome del nuovo proprietario ")
            self.proprietario = nuovo_proprietario
        elif scelta == 2:
            nuova_marca = input("inserisci la marca dell'auto ")
            self.marca = nuova_marca
        elif scelta == 3:
            nuovo_modello = input("inserisci il modello dell'auto ")
            self.modello = nuovo_modello
        elif scelta == 4:
            nuovo_cilindrata = input("inserisci la cilindrata dell'auto ")
            self.cilindrata = nuovo_cilindrata
        elif scelta == 5:
            nuovo_cavalli = input("inserisci i cavalli dell'auto ")
            self.cavalli = nuovo_cavalli
        elif scelta == 6:
            nuovo_colore = input("inserisci il colore dell'auto ")
            self.colore = nuovo_colore
        elif scelta == 7:
            nuovo_assicurazione = input(""" inserisci se il veicolo ha o meno l'assicurazione
                                            True o False """)
            self.assicurazione = nuovo_assicurazione
        elif scelta == 8:
            nuovo_garanzia = input("inserisci la garanzia dell'auto ")
            self.garanzia = nuovo_garanzia
    

# funzione che da la possibilità di scegliere se cambiare parametri o meno 
def scelta_modifica_parametri():  
    scelta = int(input("""
    modifica i parametri di un'auto:
    1 = modifica parametri prima auto 
    2 = modifica parametri second auto 
    3 = non modificare parametri
    """))
    if scelta == 1:
        auto1.modifica_parametri()
        print(auto1.scheda())
    elif scelta == 2:
        auto2.modifica_parametri()
        print(auto2.scheda())
    elif scelta == 3:
        print("""
        premi CTRL + C per uscire dal programma
        """)

# creazione istanza
auto1= auto("giovanni","ford","fiesta",1500, 160, "rosso")

#creazione istanza
auto2= auto("marco","fiat","Bravo",2500, 200, "verde")

#printo le istanze create e il numero di istanze create 
print(""" 
Le singole scheda sono:
""",
auto1.scheda(),
"""

""",
auto2.scheda(), 
"""
le auto totali sono: 
""", auto.parcoAuto)

# do la possibilità del cambio parametri
scelta_modifica_parametri()






