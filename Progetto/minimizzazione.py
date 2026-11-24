# Esercitazione su minimizzazione
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

data = pd.read_csv('http://opendata.cern.ch/record/5203/files/Jpsimumu.csv')

# Calcolo della massa invariante per ogni evento

massa_i = np.sqrt((data['E1'] + data['E2'])**2 - (
                  (data['px1'] + data['px2'])**2 + 
                  (data['py1'] + data['py2'])**2 +
                  (data['pz1'] + data['pz2'])**2))

def gauss1(x, A, m, sigma, p1, p0):
    return A * np.exp(-(x - m)**2 / (2 * sigma**2)) + p1 * x + p0

def gauss2(x, A1, A2, m, p1, p0):
    sigma_1 = np.std(massa_i)
    sigma_2 = np.std(massa_i)
    return A1 * np.exp(-(x - m)**2 / (2 * sigma_1**2)) + A2 * np.exp(-(x - m)**2 / (2 * sigma_2**2)) + p1 * x + p0

# Istogramma della massa invariante 

fig = plt.figure(figsize=(14,7))
n, bins, p = plt.hist(massa_i, bins=200, color='orange', ec='red', label='Massa invariante')

# Formattazione grafico
plt.title('Istogramma della massa invariante')
plt.xticks(np.arange(min(massa_i), max(massa_i) + 0.25, 0.25))
plt.yticks(np.arange(0, max(n) + 250, 250))
plt.xlabel('Massa invariante [GeV]')
plt.ylabel('Occorrenze')
plt.grid(True, alpha=0.3)
plt.legend()

# Mostro grafico
plt.show()

# Istogramma della massa invariante intorno al massimo
fig = plt.figure(figsize=(14,7))
n, bins, p = plt.hist(massa_i, bins=200, color='orange', ec='red', label='Massa invariante')

# Formattazione grafico
plt.title('Istogramma della massa invariante intorno al massimo')
plt.xticks(np.arange(min(massa_i), max(massa_i) + 0.25, 0.25))
plt.yticks(np.arange(0, max(n) + 250, 250))
plt.xlim(3.2 - 0.5, 3.2 + 0.5)
plt.xlabel('Massa invariante [GeV]')
plt.ylabel('Occorrenze')
plt.grid(True, alpha=0.3)
plt.legend()

# Mostro grafico
plt.show()

# Fit per ricavare i parametri
par_iniziale = np.array([350, 3.1, 0.04, 0.1, 20])
x_bins = (bins[:-1] + bins[1:]) / 2
mask = (x_bins >= 2.7) & (x_bins <= 3.7)
x_fit = x_bins[mask]
n_fit = n[mask]
err_n = np.sqrt(np.maximum(n_fit, 1))
parametri, par_cov = optimize.curve_fit(gauss1, x_fit, n_fit, p0=[par_iniziale])

# Grafico del fit
x = np.linspace(2.7, 3.7, 10000)
y = gauss1(x, *parametri)
scarto = n_fit - gauss1(x_fit, *parametri)
sigma_scarto = np.sqrt(err_n**2)
scarto_norm = scarto / err_n

# Plot del grafico
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(14,7))

# ax1
ax1.errorbar(x_fit, n_fit, yerr=err_n, color='orange', fmt='o', label='Dati')
ax1.plot(x, y, color='blue', label='Fit')

# formattazione ax1
ax1.set_xlim(2.7, 3.7)
ax1.grid(alpha=0.3)
ax1.legend()

# ax2
ax2.errorbar(x_fit, scarto, yerr= sigma_scarto, fmt='o', color='orange', label='Scarto dei dati')
ax2.plot(np.array([0, 5]), np.array([0, 0]), color='blue', label='scarto atteso')

# formattazione ax2
ax2.set_xlim(2.7, 3.7)
ax2.grid(alpha=0.3)
ax2.legend()

# ax3
ax3.errorbar(x_fit, scarto_norm, yerr = sigma_scarto, fmt='o', color='orange', label='Scarto dei dati normalizzato')
ax3.plot(np.array([0, 5]), np.array([0, 0]), color='blue', label='scarto atteso')

# formattazione ax3
ax3.set_xlim(2.7, 3.7)
ax3.grid(alpha=0.3)
ax3.legend()

plt.show()
