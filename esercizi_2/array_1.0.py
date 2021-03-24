import numpy as np

n1 = int(input("inseriswci un 1° numero intero "))
n2 = int(input("inseriswci un 2° numero intero "))
n3 = int(input("inseriswci un 3° numero intero "))
n4 = int(input("inseriswci un 4° numero intero "))
n5 = int(input("inseriswci un 5° numero intero "))

dati = np.array ( [n1,n2,n3,n4,n5] )

lista = [n1,n2,n3,n4,n5]

lista.sort()

print (lista)

lista.reverse()

print(lista)