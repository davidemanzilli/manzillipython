import matplotlib.pyplot as plt
import numpy as np

#grafico prima legge di gay lussac
plt.title("la prima legge di gay lussac")
plt.xlabel("volume") 
plt.ylabel("pressione")
xpoints = np.array([0,1,2,3,4,5])
ypoints = np.array([1 for i in range(len(xpoints+1))])
plt.plot(xpoints, ypoints)
plt.show()
