import matplotlib.pyplot as plt
import numpy as np

#grafico spazio tempo nel MRU
plt.title("la velocita nel moto rettilineo uniforme")
plt.xlabel("spazio") 
plt.ylabel("tempo")
xpoints = np.array([0,1,2,3,4,5])
ypoints = np.array([0,1,2,3,4,5])
plt.plot(xpoints, ypoints)
plt.show()