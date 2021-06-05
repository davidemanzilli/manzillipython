import numpy as np

tabella = {
    "materia" :["matematica", "italiano", "scienze", "inglese"],
    "mario":[6, 6, 7, 4,], 
    "Giovanni":[4, 6, 5, 4], 
    "Paola":[9, 6, 8, 8] 
}

print (tabella)


print ("la media di Mario è", np.mean(tabella["mario"]))
print ("la media di Giovanni è", np.mean(tabella["Giovanni"]))
print ("la media di Paola è", np.mean(tabella["Paola"]))
