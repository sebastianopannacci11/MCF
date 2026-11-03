# File di definizione delle funzioni per il progetto
import numpy as np
from scipy.stats import norm, gamma, uniform

def genera_pacchetto_onda_discreto(
    N = 100,
    freq_dist= norm(loc=5.0, scale=1.0),
    amp_mode = 'pdf',
    amp_dist = uniform(loc=0.1, scale=0.9),
    coherent_phase = True,
    x_range = (-10, 10),
    points = 1000
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

    # Generazione dei numeri d'onda k_i dalla distribuzione scelta
    k_components = freq_dist.rvs(size=N)

    # Definizione delle ampiezze
    if amp_mode == 'pdf':
        # Densità di probabilità della frequenza k_i
        amplitudes = freq_dist.pdf(k_components)
    elif amp_mode == 'dist':
        # Ampiezze estratte in modo stocastico da una seconda distribuzione
        amplitudes = amp_dist.rvs(size=N)
    else:
        raise ValueError("amp_mode deve essere 'pdf' o 'dist'")
    
    return 