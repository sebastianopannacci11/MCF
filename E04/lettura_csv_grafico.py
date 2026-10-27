from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

csv_path = Path(__file__).parent.parent / "kplr010666592-2011240104155_slc.csv"
dataframe = pd.read_csv("kplr010666592-2011240104155_slc.csv")

print(*dataframe.columns.tolist())

# Grafico del flusso in funzione del tempo
# Dati grafico
x1 = dataframe['TIME']
y1 = dataframe['PDCSAP_FLUX']

# Grafico
plt.figure(figsize=(12, 6))
plt.plot(x1, y1, 'o', color='blue', label='flusso')

# Formattazione grafico
plt.title('Grafico', fontsize=13, fontweight='bold')
plt.xlabel('Tempo [$s$]', fontsize=11)
plt.ylabel('Flusso di elettroni [$e^-/s$]', fontsize=11)
plt.xlim(left=x1.min(), right=x1.max())
plt.ylim(bottom=y1.min(), top=y1.max())
plt.xticks(np.arange(x1.min(), x1.max(), 2))
plt.yticks(np.arange(y1.min(), y1.max(), 0.001e6))
plt.grid('--')
plt.legend()

# Mostro Grafici
plt.show()

# Errori grafico
sigma_y1 = dataframe['PDCSAP_FLUX_ERR']

# Grafico con barre di errore

plt.figure(figsize=(12, 6))
plt.errorbar(x1, y1, yerr=sigma_y1, elinewidth=2, fmt='o', color='blue', label='flusso')

# Formattazione grafico
plt.title('Grafico del flusso di elettroni nel tempo', fontsize=13, fontweight='bold')
plt.xlabel('Tempo [$BJD - 2454833$]', fontsize=11)
plt.ylabel('Flusso di elettroni [$e^-/s$]', fontsize=11)
plt.xlim(left=x1.min(), right=x1.max())
plt.ylim(bottom=y1.min(), top=y1.max())
plt.xticks(np.arange(x1.min(), x1.max(), 2))
plt.yticks(np.arange(y1.min() - sigma_y1.max(), y1.max() + sigma_y1.max(), 0.001e6))
plt.grid('--')
plt.legend()

# Mostro Grafico
plt.show()

# Funzione per chiedere se salvare in pdf o in png
def chiedi_conferma(messaggio):
    risposta = ""
    while risposta not in ["y", "n"]:
        risposta = input(f"{messaggio} [y/n]: ").strip().lower()
    return risposta == "y"

if chiedi_conferma("Salvare il grafico?"):
    if chiedi_conferma("Salvare in .png?"):
        plt.savefig("grafico.png", dpi=300, bbox_inches="tight")
        print("Salvato in .png.")

    if chiedi_conferma("Salvare in .pdf?"):
        plt.savefig("grafico.pdf", bbox_inches="tight")
        print("Salvato in .pdf.")

# Grafico con intervallo selezionato di tempo intorno al primo minimo

dataframe_minimo = dataframe.loc[(dataframe['TIME'] < 948.3) & (dataframe['TIME'] > 947.9)]

# Dati per il grafico

x2 = dataframe_minimo['TIME']
y2 = dataframe_minimo['PDCSAP_FLUX']
sigma_y2 = dataframe_minimo['PDCSAP_FLUX_ERR']

# Grafico con barre di errore intorno al minimo

plt.figure(figsize=(12, 6))
plt.errorbar(x2, y2, yerr=sigma_y2, elinewidth=2, fmt='o', color='blue', label='flusso di elettroni')

# Formattazione grafico
plt.title('Grafico del flusso intorno al minimo', fontsize=13, fontweight='bold')
plt.xlabel('Tempo [$BJD - 2454833$]', fontsize=11)
plt.ylabel('Flusso di elettroni [$e^-/s$]', fontsize=11)
plt.xlim(left=x2.min(), right=x2.max())
plt.ylim(bottom=y2.min(), top=y2.max())
plt.xticks(np.arange(x2.min(), x2.max(), 0.05))
plt.yticks(np.arange(y2.min() - sigma_y2.max(), y2.max() + sigma_y2.max(), 0.0005e6))
plt.grid('--')
plt.legend()

# Mostro Grafico
plt.show()

# Grafico complessivo con vista generale e zoom intorno al primo minimo

fig, ax = plt.subplots(figsize=(12,6))

ax.errorbar(x1, y1, sigma_y1, marker='o', color='blue', label='flusso di elettroni')
ax.set_title('Grafico del flusso di elettroni in funzione del tempo', fontsize=13, fontweight='bold')
ax.set_xlabel('Tempo [$BJD - 2454833$]', fontsize=11)
ax.set_ylabel('Flusso di elettroni [$e^-/s$]', fontsize=11)
ax.set_xlim(left=x1.min(), right=x1.max())
ax.set_ylim(bottom=y1.min(), top=y1.max())
ax.set_xticks(np.arange(x1.min(), x1.max(), 2))
ax.set_yticks(np.arange(y1.min() - sigma_y1.max(), y1.max() + 0.008e6, 0.001e6))
ax.grid('--')
ax.legend()

ax_inset = ax.inset_axes([0.55, 0.55, 0.38, 0.38])
ax_inset.errorbar(x2, y2, color="red", marker="o", markersize=3)
ax_inset.tick_params(labelsize=8)
ax_inset.grid('--')

plt.show()

if chiedi_conferma("Salvare il grafico?"):
    if chiedi_conferma("Salvarlo in .png?"):
        plt.savefig("grafico_intorno.png", dpi=300)
        print("Salvato in .png.")

    if chiedi_conferma("Vuoi salvarlo in .pdf?"):
        plt.savefig("grafico_intorno.pdf", bbox_inches="tight")
        print("Salvato in .pdf.")