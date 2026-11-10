import rndwalk as rw
import numpy as np
import matplotlib.pyplot as plt

# Esempio di utilizzo della funzione random_walk con 5 random walker
# Dati
passi = 1000
s = 1

plt.figure(figsize=(12, 6))
for i in range(5):
    delta_x, delta_y = rw.random_walk(s, passi)
    plt.plot(delta_x, delta_y, alpha=0.7, label=f'Walker {i+1}')

plt.show()

# Grafico con due grafici contemporanei: uno con la distribuzione dei passi e uno con la distribuzione dei raggi
fig, ax = plt.subplots(1, 2, figsize=(12,6))
for i in range(5):
    delta_x, delta_y = rw.random_walk(s, passi)
    ax[0].plot(delta_x, delta_y, alpha=0.7, label=f'Walker {i+1}')
    ax[1].plot(delta_x**2 + delta_y**2, alpha=0.7, label=f'Walker {i+1}')
plt.show()