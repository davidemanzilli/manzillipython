alfabeto=["a","b","c","d",]
parola = "paarola"
conteggio = 0
for carattere in parola:
    if carattere in alfabeto:
        conteggio = conteggio + 1
print ("ci sono",conteggio,"a")