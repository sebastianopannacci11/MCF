import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, gamma, uniform
import Moduli as mod

# --- Esempio d'uso e Visualizzazione ---
x, signal, k_sampled, A_sampled = mod.generate_wave_packet(
    N=200, 
    freq_dist=norm(loc=6.0, scale=0.5), # Gaussiana attorno a k=6
    amp_mode='pdf',
    coherent_phase=True
)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6), gridspec_kw={'height_ratios': [2, 1]})

# Grafico del pacchetto d'onda nello spazio
ax1.plot(x, signal, color='#1f77b4', lw=1.2, label='Pacchetto d\'onda $y(x)$')
ax1.set_title('Pacchetto d\'onda nello spazio $x$')
ax1.set_ylabel('Ampiezza')
ax1.grid(True, alpha=0.3)
ax1.legend()

# Grafico dello spettro discreto di frequenze/ampiezze campionate
ax2.stem(k_sampled, A_sampled, linefmt='r-', markerfmt='ro', basefmt=' ', label='Componenti $A_i(k_i)$')
ax2.set_title('Distribuzione discreta delle frequenze $k_i$ e ampiezze $A_i$')
ax2.set_xlabel('Numero d\'onda $k$')
ax2.set_ylabel('Ampiezza $A_i$')
ax2.grid(True, alpha=0.3)
ax2.legend()

plt.tight_layout()
plt.show()
