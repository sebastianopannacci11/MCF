import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataframe = pd.read_csv("ExoplanetsPars_2025.csv", comment="#")

print(*dataframe.columns.tolist())

print(dataframe)

# Grafico con assi logaritmici della massa del pianeta in funzione del periodo orbitale

# Dati
x = dataframe['pl_orbper']
y = dataframe['pl_bmassj']

plt.figure(figsize=(12, 6))
plt.scatter(x, y, color='blue', label='Esopianeti')

# Formattazione grafico
plt.title('Massa del pianeta in funzione del periodo orbitale', fontsize=13, fontweight='bold')
plt.xlabel('Periodo orbitale [$days$]', fontsize=11)
plt.ylabel('Massa del pianeta [$M_{Jup}$]', fontsize=11)
plt.xscale('log')
plt.yscale('log')
plt.grid(True, which='major', linestyle='-', linewidth=0.8, color='black', alpha=0.7)
plt.grid(True, which='minor', linestyle='--', linewidth=0.5, color='gray', alpha=0.5)
plt.legend()

# Mostro Grafici
plt.show()

# Grafico con assi logaritmici della grandezza R^2_max /m* in funzione del periodo orbitale

# Dati
x = dataframe['pl_orbper']
y = dataframe['pl_orbsmax']**2 / dataframe['st_mass']

plt.figure(figsize=(12, 6))
plt.scatter(x, y, color='blue', label='Esopianeti')

# Formattazione grafico
plt.title('R^2_max /m* in funzione del periodo orbitale', fontsize=13, fontweight='bold')
plt.xlabel('Periodo orbitale [$days$]', fontsize=11)
plt.ylabel(r'$R^2_{max} /m_* [m^2/m_{\odot}]$', fontsize=11)
plt.xscale('log')
plt.yscale('log')
plt.grid(True, which='major', linestyle='-', linewidth=0.8, color='black', alpha=0.7)
plt.grid(True, which='minor', linestyle='--', linewidth=0.5, color='gray', alpha=0.5)
plt.legend()

# Mostro Grafici
plt.show()