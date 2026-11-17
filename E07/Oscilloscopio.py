# Oscilloscopio
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Funzione per le derivata con la differenza centrale
# f'(i) =  [f(i+n)-f(i-n)] / [x(i+n)-x(i-n)]
def derivata(x, y, n=1):
    '''
    Metodo che calcola la derivata (differenza centrale):
    input:
    - x: punti;
    - y: funzione dei punti x;
    - n: distanza dal punto x;
    '''
    x = np.asarray(x)
    y = np.asarray(y)
    dy = y[2*n:] - y[:-2*n]
    dx = x[2*n:] - x[:-2*n]
    
    return x[n:-n], dy / dx

# dati importati da oscilloscopio.csv

dati = pd.read_csv('oscilloscope.csv')

tempo = dati['time']
segnale1 = dati['signal1']
segnale2 = dati['signal2']

# Grafico di segnale 1 vs segnale 2
plt.figure(figsize=(14, 7))

# plot del grafico
plt.plot(segnale1, segnale2, color='orangered', label='segnale1 vs segnale2')

# Formattazione del grafico
plt.title('Segnale 1 vs segnale 2')
plt.xlabel('Segnale 1')
plt.ylabel('Segnale 2')
plt.xticks(np.arange(-80, 20, 5))
plt.yticks(np.arange(-60, 10, 20))
plt.grid(True, alpha=0.3)
plt.legend()

# Mostro il grafico
plt.show()

# Grafico dei segnali in funzione del tempo
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

ax1.plot(tempo, segnale1, color='green', label=r'$segnale 1$')
ax2.plot(tempo, segnale2, color='purple', label=r'$segnale 2$')

# Formattazione del grafico 
ax1.set_title('Tempo vs segnale 1')
ax2.set_title('Tempo vs segnale 2')
ax1.set_xlabel('Tempo')
ax2.set_xlabel('Tempo')
ax1.set_ylabel('Segnale 1')
ax2.set_ylabel('Segnale 2')
ax1.set_xticks(np.arange(0, max(tempo), 5000))
ax2.set_xticks(np.arange(0, max(tempo), 5000))
ax1.set_yticks(np.arange(min(segnale1), max(segnale1) + 0.1 , 10))
ax2.set_yticks(np.arange(min(segnale2), max(segnale2) + 0.1 , 10))
ax1.grid(True, alpha=0.3)
ax2.grid(True, alpha=0.3)
ax1.legend()
ax2.legend()
plt.tight_layout()

# Mostro il grafico
plt.show()

# Calcolo della derivata del grafico 
n = 100
m = 100

tempi1, der1 = derivata(tempo, segnale1, n)
tempi2, der2 = derivata(tempo, segnale2, m)

# Grafico dei segnali in funzione del tempo
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

ax1.plot(tempi1, der1, color='green', label=r'$segnale 1$')
ax2.plot(tempi2, der2, color='purple', label=r'$segnale 2$')

# Formattazione del grafico 
ax1.set_title(f'Derivata del segnale 1 con n = {n}')
ax2.set_title(f'Derivata del segnale 2 con n = {m}')
ax1.set_xlabel('Tempo')
ax2.set_xlabel('Tempo')
ax1.set_ylabel('Derivata del segnale 1')
ax2.set_ylabel('Derivata del segnale 2')
ax1.set_xticks(np.arange(0, max(tempo), 5000))
ax2.set_xticks(np.arange(0, max(tempo), 5000))
ax1.set_yticks(np.arange(min(der1), max(der1) + 0.01 , 0.2))
ax2.set_yticks(np.arange(min(der2), max(der2) + 0.01 , 0.2))
ax1.grid(True, alpha=0.3)
ax2.grid(True, alpha=0.3)
ax1.legend()
ax2.legend()
plt.tight_layout()

# Mostro il grafico
plt.show()

# Minimi delle funzioni (posizione e funzione del minimo)

s1_rid = np.asarray(segnale1)[n:-n]
s2_rid = np.asarray(segnale2)[m:-m]

# Maschera booleana per i minimi locali:
# 1) Cambio di segno della derivata da negativa a positiva (identifica solo i minimi, non i massimi)
# 2) Filtro sull'ampiezza (sotto media - std) per ignorare le piccole oscillazioni di rumore sulla baseline
mask_min1 = (der1[:-1] < 0) & (der1[1:] >= 0) & (s1_rid[:-1] < np.mean(s1_rid) - np.std(s1_rid))
mask_min2 = (der2[:-1] < 0) & (der2[1:] >= 0) & (s2_rid[:-1] < np.mean(s2_rid) - np.std(s2_rid))

# Posizioni (tempi) e valori dei minimi trovati
t_min1, val_min1 = tempi1[:-1][mask_min1], s1_rid[:-1][mask_min1]
t_min2, val_min2 = tempi2[:-1][mask_min2], s2_rid[:-1][mask_min2]

print("Segnale 1 - Tempi dei minimi:", t_min1)
print("Segnale 1 - Valori dei minimi:", val_min1)
print("Segnale 2 - Tempi dei minimi:", t_min2)
print("Segnale 2 - Valori dei minimi:", val_min2)

# Grafico di verifica con i minimi evidenziati sui segnali originali
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))
ax1.plot(tempo, segnale1, color='green', label='Segnale 1')
ax1.scatter(t_min1, val_min1, color='red', zorder=5, label='Minimi trovati')
ax2.plot(tempo, segnale2, color='purple', label='Segnale 2')
ax2.scatter(t_min2, val_min2, color='red', zorder=5, label='Minimi trovati')

ax1.set_title('Minimi Segnale 1')
ax2.set_title('Minimi Segnale 2')
ax1.set_xlabel('Tempo')
ax2.set_xlabel('Tempo')
ax1.set_ylabel('Segnale 1')
ax2.set_ylabel('Segnale 2')
ax1.grid(True, alpha=0.3)
ax2.grid(True, alpha=0.3)
ax1.legend()
ax2.legend()
plt.tight_layout()
plt.show()