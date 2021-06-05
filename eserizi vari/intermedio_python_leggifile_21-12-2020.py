import string
import numpy as np
import matplotlib.pyplot as plt


# apriamo il file in lettura
f = open("dati.txt", 'r')

# usiamo il metodo readlines 
# per ottenere una lista di righe del file

# stampiamo la prima riga
# print(f.readline()) 

# possiamo fare un ciclo e prendere riga per riga 

coordX = []
coordY = []



# da notare che posso fare un ciclo all'interno di un file
# direttamente sulle righe

for riga in f:
    valori = str(f.readline())  # converto in stringa la riga
    Nval = len(valori)          # conto il numero di caratteri
    valori = valori.strip('\n') # elimino i lterminatore di riga
    valori = valori.split(',')  # separo la stringa in due numeri
    valori = list(valori)       # converto in lista
    print(valori)
    coordX.append(int(valori[0])) # aggiungo la coordinata X
    coordY.append(int(valori[1])) # aggiungo la coordinata Y

f.close()  # chiudiamo il file

print ("X: ",coordX)
print ("Y: ",coordY)


# ordiniamo le liste
coordX.sort()
coordY.sort()


print("liste ordinate:") 
print ("X: ",coordX)
print ("Y: ",coordY)


# stampo il tipo di dati delle coordinate
print(type(coordX))
print(type(coordY))


# ora sono pronte per essere usate anche nei grafici


plt.scatter(coordX,coordY, color='red', alpha=0.5, marker='.')
plt.title("GRAFICO A DISPERSIONE", color='#003399')
plt.ylabel('Y', color='#003399')
plt.xlabel('X', color='#003399')
plt.xticks([10*k for k in range(0,11)])
plt.yticks([10*k for k in range(0,11)])

plt.show()
