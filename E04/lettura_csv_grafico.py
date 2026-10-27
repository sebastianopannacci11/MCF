from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

csv_path = Path(__file__).parent / "kplr010666592-2011240104155_slc.csv"
dataframe = pd.read_csv(csv_path)

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
plt.yticks(np.arange(y1.min(), y1.max(), 1.001e6))
plt.legend()

# Mostro Grafici
plt.show()

# Errori grafico
sigma_y1 = dataframe['PDCSAP_FLUX_ERR']

# Grafico con barre di errore

plt.figure(figsize=(12, 6))
plt.errorbar(x1, y1, yerr=sigma_y1, elinewidth=2, fmt='o', color='blue', label='flusso')

# Formattazione grafico
plt.title('Grafico', fontsize=13, fontweight='bold')
plt.xlabel('Tempo [$BJD - 2454833$]', fontsize=11)
plt.ylabel('Flusso di elettroni [$e^-/s$]', fontsize=11)
plt.xlim(left=x1.min(), right=x1.max())
plt.ylim(bottom=y1.min(), top=y1.max())
plt.xticks(np.arange(x1.min(), x1.max(), 2))
plt.yticks(np.arange(y1.min(), y1.max(), 1.001e6))
plt.legend()

# Mostro Grafici
plt.show()

# Funzione per chiedere se salvare in pdf o in png
def chiedi_conferma(messaggio):
    risposta = ""
    while risposta not in ["y", "n"]:
        risposta = input(f"{messaggio} [y/n]: ").strip().lower()
    return risposta == "y"

if chiedi_conferma("Vuoi salvare il grafico?"):
    if chiedi_conferma("Vuoi salvarlo in .png?"):
        plt.savefig("grafico.png", dpi=300, bbox_inches="tight")
        print("-> Salvato in PNG.")

    if chiedi_conferma("Vuoi salvarlo in .pdf?"):
        plt.savefig("grafico.pdf", bbox_inches="tight")
        print("-> Salvato in PDF.")

# Grafico con intervallo selezionato di tempo intorno al primo minimo

dataframe_minimo = dataframe.loc[(dataframe['Time'] < 948.3) & (dataframe['Time'] > 947.9)]

# Dati per il grafico

x2 = dataframe_minimo['TIME']
y2 = dataframe_minimo['PDCSAP_FLUX']
sigma_y2 = dataframe_minimo['PDCSAP_FLUX_ERR']

