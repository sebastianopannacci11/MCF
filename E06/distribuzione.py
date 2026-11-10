import numpy as np
import sys
import scipy
import matplotlib.pyplot as plt

# Funzione 3/1000 x^2 con metodo hit / miss

def distr_hit_miss(x):
    """
    Funzione di distribuzione (3/1000) * x^2 per x in [0, 10].
    
    Parameters: x : array-like
        Valori di x per cui calcolare la distribuzione.
    
    Returns: array-like
        Valori della distribuzione per i valori di x forniti.
    """

    return (3/1000) * x**2

def distr_cumul(x):
    """
    Funzione di distribuzione cumulativa della distribuzione (3/1000) * x^2 per x in [0, 10].
    C(x) = (1/1000) * x^3
    
    Parameters: x : array-like
        Valori di x per cui calcolare la distribuzione cumulativa.
    
    Returns: array-like
        Valori della distribuzione cumulativa per i valori di x forniti.
    """
    
    return x**3 / 1000

def distr_cumul_inv(z):
    """
    Funzione inversa della distribuzione cumulativa della distribuzione (3/1000) * x^2 per x in [0, 10].
    C^-1(z) = (1000 * z)^(1/3)
    
    Parameters: z : array-like
        Valori di z per cui calcolare la distribuzione cumulativa inversa.
    
    Returns: array-like
        Valori della distribuzione cumulativa inversa per i valori di z forniti.
    """
    
    return 10 * z**(1/3)

# Esempio di utilizzo della distribuzione hit/miss

n_samples = 100000

x = np.random.uniform(low=0, high=10, size=n_samples) # distribuzione uniforme tra 0 e 10
y = np.random.uniform(low=0, high=3/10, size=n_samples) # distribuzione uniforme tra 0 e 3/10

# Grafico della distribuzione hit/miss
plt.figure(figsize=(12, 6))

mask = y <= distr_hit_miss(x)
x_hit = x[mask]
y_hit = y[mask]
plt.scatter(x_hit, y_hit, color='red', label='Distribuzione Hit/Miss')

# Formattazione grafico
plt.title(r'Distribuzione Hit/Miss per la funzione $f(x) = \frac{3}{1000}x^2$', fontsize=13, fontweight='bold')
plt.xlabel('x hit or miss', fontsize=11)
plt.ylabel('y hit or miss', fontsize=11)
plt.grid('--', alpha=0.5)
plt.legend()

# Mostro grafico 
plt.show()

# Istogramma dei valori x selezionati
plt.hist(x, bins=100, range=(0,5), color='red', label='Valori X Generati')
plt.hist(x_hit, bins=100, range=(0,5), color='blue', label='Valori X Selezionati')
plt.xlabel('X')
plt.legend()
plt.show()

# Esempio di utilizzo della distribuzione cumulativa

z = np.random.uniform(low=0, high=1, size=n_samples) # distribuzione uniforme tra 0 e 1
x = distr_cumul(z) # distribuzione cumulativa

# Grafico della distribuzione cumulativa
plt.figure(figsize=(12, 6))
plt.scatter(z, x, color='blue', label='Distribuzione Cumulativa')
# Formattazione grafico
plt.title(r'Distribuzione Cumulativa per la funzione $C(x) = \frac{1}{1000}x^3$', fontsize=13, fontweight='bold')
plt.xlabel('z', fontsize=11)
plt.ylabel('x', fontsize=11)
plt.grid('--', alpha=0.5)
plt.legend()

# Mostro grafico
plt.show()

# Esempio di utilizzo della distribuzione cumulativa

z = np.random.uniform(low=0, high=1, size=n_samples) # distribuzione uniforme tra 0 e 1
x = distr_cumul_inv(z) # distribuzione cumulativa

# Grafico della distribuzione cumulativa inversa
plt.figure(figsize=(12, 6))
plt.scatter(x, z, color='blue', label='Distribuzione Cumulativa Inversa')
# Formattazione grafico
plt.title(r'Distribuzione Cumulativa Inversa per la funzione $C^{-1}(z) = (1000z)^{1/3}$', fontsize=13, fontweight='bold')
plt.xlabel('z', fontsize=11)
plt.ylabel('x', fontsize=11)
plt.grid('--', alpha=0.5)
plt.legend()

# Mostro grafico
plt.show()

fig, ax = plt.subplots(1,2, figsize=(11,5))
ax[0].hist(z, bins=100, range=(0,1), color='cyan',   ec='darkcyan')
ax[0].set_title('Distribuzione y Cumulativa')
ax[0].set_xlabel('y cumulativa')

ax[1].hist(x, bins=100, range=(0,5), color='orange', ec='darkorange')
ax[1].set_title('Distribuzione secondo la funzione Onda Quadra')
ax[1].set_xlabel('x')
plt.show()