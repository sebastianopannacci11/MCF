import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataframe = pd.read_csv("ExoplanetsPars_2025.csv", comment="#")

print('Colonne:', dataframe.columns)

print(dataframe)

# Pianeti del Sistema Solare
ss_orbper  = np.array( [ 88, 225, 365, 687, 4333, 10759, 30687, 60190])
ss_orbsmax = np.array( [ 0.47, 0.73, 1.02, 1.67, 5.45, 10.07, 20.09, 30.32])

ss_bmasse = np.array( [ 0.06, 0.82, 1.0, 0.11, 317.89,  95.17, 14.56, 17.24, ] )
ss_bmassj = ss_bmasse/317.89

# Grafico con assi logaritmici della massa del pianeta in funzione del periodo orbitale

# Dati
x = dataframe['pl_orbper']
y = dataframe['pl_bmassj']

plt.figure(figsize=(12, 6))
plt.scatter(x, y, color='blue', label='Esopianeti', alpha=0.5)
plt.scatter(ss_orbper, ss_bmassj, color='red', label='Pianeti Sistema Solare', alpha=0.5)

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
plt.scatter(x, y, color='blue', label='Esopianeti', alpha=0.5)
plt.scatter(ss_orbper, ss_orbsmax**2, color='red', label='Pianeti Sistema Solare', alpha=0.5)

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

# Grafico massa del pianeta in funzione del periodo orbitale

# Dati
plt.figure(figsize=(12, 6))
plt.scatter(dataframe.loc[dataframe['discoverymethod'] == 'Transit', 'pl_orbper'],
            dataframe.loc[dataframe['discoverymethod'] == 'Transit', 'pl_bmassj'], color='blue', label='Transit', alpha=0.5)
plt.scatter(dataframe.loc[dataframe['discoverymethod'] == 'Radial Velocity', 'pl_orbper'],
            dataframe.loc[dataframe['discoverymethod'] == 'Radial Velocity', 'pl_bmassj'], color='green', label='Radial Velocity', alpha=0.5)
plt.scatter(ss_orbper, ss_bmassj, color='red', label='Pianeti Sistema Solare', alpha=0.5)

# Formattazione grafico
plt.title('Massa del pianeta in funzione del periodo orbitale', fontsize=13, fontweight='bold')
plt.xlabel('Periodo orbitale [$days$]', fontsize=11)
plt.ylabel(r'$M_{planet} [M_{Jup}]$', fontsize=11)
plt.xscale('log')
plt.yscale('log')
plt.grid(True, which='major', linestyle='-', linewidth=0.8, color='black', alpha=0.7)
plt.grid(True, which='minor', linestyle='--', linewidth=0.5, color='gray', alpha=0.5)
plt.legend()

# Mostro Grafici
plt.show()

# Istogramma massa del pianeta
fig = plt.figure(figsize=(12, 6))

gs = fig.add_gridspec(2, 2, hspace=0, wspace=0)
ax = gs.subplots( sharex='col', sharey='row')

ax[1,0].scatter( np.log10(dataframe.loc[dataframe['discoverymethod']=='Transit', 'pl_orbper']),
                 np.log10(dataframe.loc[dataframe['discoverymethod']=='Transit',  'pl_bmassj']), color='limegreen',  alpha=0.3, label='Transit')
ax[1,0].scatter( np.log10(dataframe.loc[dataframe['discoverymethod']=='Radial Velocity', 'pl_orbper']),
                 np.log10(dataframe.loc[dataframe['discoverymethod']=='Radial Velocity', 'pl_bmassj']), color='darkorange', alpha=0.3, label='Radial Velocity')
ax[1,0].scatter(np.log10(ss_orbper), np.log10(ss_bmassj), color='slategray', label='Solar System')

# Formattazione grafico
ax[1,0].set_xlabel('log(Period [days])',         fontsize=16)
ax[1,0].set_ylabel(r'log(Planet Mass [$m_J$])',  fontsize=16)
ax[1,0].legend(fontsize=16)

# Istogramma Periodo
ax[0,0].hist( np.log10(dataframe.loc[dataframe['discoverymethod']=='Transit', 'pl_orbper']),
              bins=50, range=(-2, 5), color='limegreen',  alpha=0.5, label='Transit')

ax[0,0].hist( np.log10(dataframe.loc[dataframe['discoverymethod']=='Radial Velocity', 'pl_orbper']),
              bins=50, range=(-2, 5), color='darkorange',  alpha=0.5, label='Radial Velocity')
ax[0,0].tick_params(axis='both', which='major', labelsize=14)
ax[0,0].set_ylabel(r'Number of planets',        fontsize=16)
ax[0,0].legend(fontsize=16)


# Istogramma Massa pianeta
ax[1,1].hist( np.log10(dataframe.loc[dataframe['discoverymethod']=='Transit', 'pl_bmassj']),
              bins=50, range=(-4, 4), color='limegreen',  alpha=0.5, orientation='horizontal', label='Transit')

ax[1,1].hist( np.log10(dataframe.loc[dataframe['discoverymethod']=='Radial Velocity', 'pl_bmassj']),
              bins=50, range=(-4, 4), color='darkorange',  alpha=0.5, orientation='horizontal', label='Radial Velocity')

ax[1,1].tick_params(axis='both', which='major', labelsize=14)
ax[1,1].set_xlabel( 'Number of planets',        fontsize=16)
ax[1,1].legend(fontsize=16)

# Rimuovo assi per riquadro non necessario
ax[0,1].axis('off')

plt.savefig('Exoplanets_Period_vs_Mass_Detection.pdf')
plt.savefig('Exoplanets_Period_vs_Mass_Detection.png')
plt.show()