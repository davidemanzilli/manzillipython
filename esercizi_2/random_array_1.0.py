import random 
import numpy as np

lista = []

x = 0
while x < 5:
    y = random.randint(1,8)
    print(y)
    lista = lista + [y]
    x = x+1
print(lista)

array = np.array([lista])
print(array)

scelta = int(input("scegli uno dei numeri della lista "))

x = 0
y = 0

while x < 5:
    if lista[x] == scelta:
        y = y + 1
    x = x+1
print("il numero si ripete",y, "volte")
