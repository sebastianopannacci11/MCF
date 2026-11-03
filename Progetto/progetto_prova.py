import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, gamma, uniform

def generate_wave_packet(
    N=150, 
    freq_dist=norm(loc=5.0, scale=0.8), 
    amp_mode='pdf', 
    amp_dist=uniform(loc=0.1, scale=0.9),
    coherent_phase=True,
    x_range=(-20, 20),
    points=2000
):
    """
    Genera un pacchetto d'onda sommando N componenti spettrali.
    
    Parametri:
    - N: numero di componenti (frequenze/numeri d'onda)
    - freq_dist: oggetto scipy.stats per campionare i numeri d'onda k
    - amp_mode: 'pdf' (ampiezza pesata sulla PDF della frequenza) o 'dist' (estratta da amp_dist)
    - amp_dist: oggetto scipy.stats per ampiezze casuali indipendenti (se amp_mode='dist')
    - coherent_phase: True per fasi nulle (pacchetto localizzato), False per fasi casuali [0, 2pi)
    - x_range: dominio spaziale (x_min, x_max)
    - points: risoluzione della griglia spaziale
    """
    x = np.linspace(x_range[0], x_range[1], points)
    
    # 1. Campionamento dei numeri d'onda (k_i) dalla distribuzione scelta
    k_components = freq_dist.rvs(size=N)
    
    # 2. Definizione delle ampiezze (A_i)
    if amp_mode == 'pdf':
        # L'ampiezza di ciascuna componente è data dalla densità di probabilità di k_i
        amplitudes = freq_dist.pdf(k_components)
    elif amp_mode == 'dist':
        # Ampiezze estratte in modo stocastico da una seconda distribuzione
        amplitudes = amp_dist.rvs(size=N)
    else:
        raise ValueError("amp_mode deve essere 'pdf' o 'dist'")
        
    # Normalizzazione delle ampiezze per mantenere la somma unitaria nel centro
    amplitudes /= np.sum(amplitudes)
    
    # 3. Definizione delle fasi (phi_i)
    if coherent_phase:
        phases = np.zeros(N)
    else:
        phases = np.random.uniform(0, 2 * np.pi, size=N)
        
    # 4. Sovrapposizione vettoriale (broadcasting NumPy: matrice N x points)
    # k_components[:, None] ha forma (N, 1), x ha forma (points,) -> risultato (N, points)
    waves = amplitudes[:, None] * np.cos(k_components[:, None] * x + phases[:, None])
    wave_packet = np.sum(waves, axis=0)
    
    return x, wave_packet, k_components, amplitudes

# --- Esempio d'uso e Visualizzazione ---
x, signal, k_sampled, A_sampled = generate_wave_packet(
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
