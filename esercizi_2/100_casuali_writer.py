import random

f = open("testo.txt", "w")

dati = ""

for i in range(0,100):
    dati = dati + str(random.randint(0,100)) + "\n"

f.write(dati)

f.close()

print(dati)


